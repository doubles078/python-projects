#Tapology scraper I made to gather all of the mma gyms in the US
#Built in a Jupyter Notebook then exported to this file as a backup.  Will comment and clean later.

import requests
import pandas as pd
import urllib
from bs4 import BeautifulSoup

#List of all the states to append to the URL
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

state_dfs = []

#Go through all of the Tapology.com State list pages and take the data
for state in states:
    r=requests.get("http://www.tapology.com/gyms/state/"+state, verify=False)
    c=r.content

    soup=BeautifulSoup(c, "html.parser")
    all_gyms=soup.find_all("tr")

    l=[]
    counter = 0

    for gym in all_gyms:
        d={}
        rows = gym.find_all('td', {"class": "noBorder"})
        counter = 0

        for row in rows:
            if counter == 0:
                d["Name"] = row.text
                d["Link"] = row.find('a').get('href')
                counter += 1
            elif counter == 1:
                d["Location"] = row.text
                counter += 1
            elif counter == 2:
                d["Phone"] = row.text
                counter +=1
            else:
                try:
                    site = row.find('a')
                    d["Website"] = site.get('href')
                    counter = 0
                except:
                    d["Website"] = ""
                    counter = 0
        l.append(d)

    #List comprehension to remove all blank objects within our list
    l[:] = [x for x in l if x != {}]

    #Put it into a DataFrame for usage in a Jupyter Notebook
    df = pd.DataFrame(l)
    state_dfs.append(df)

#Need to figure out why the 'for social' loop is not matching the strings.
import urllib3
urllib3.disable_warnings()

#Use the list of links scraped from the first pull to go into the detail pages for each gym and pull relevant information.
new_gyms = []

for gym in state_dfs:
    n=[]
    count = 0
    for index, row in gym.iterrows():
        new_r=requests.get("http://www.tapology.com"+row['Link'], verify=False)
        new_c=new_r.content

        new_soup=BeautifulSoup(new_c, "html.parser")
        new_all_gyms=new_soup.find_all("div", {"class": "details"})

        new_gyms.append(new_all_gyms)

        rows2 = new_gyms[index][0].find_all('a')

        socials = ['Facebook', 'Yelp', 'Twitter', 'Official Site']
        f={}
        gymname = new_soup.find_all("div", {"class": "pageHeading"})
        f['Gym'] = gymname[0].find('h1').text

        try:
            f['Logo'] = new_all_gyms[0].img['src']
        except:
            f['Logo'] = ''


        count += 1
        print(count)
        for row2 in rows2:
            if row2.text in socials:
                f[row2.text] = row2.get('href')

        n.append(f)

count = 0
for df in state_dfs:
    df.to_excel(writer,sheet_name=states[count], index=False)
    writer.save()
    count += 1
