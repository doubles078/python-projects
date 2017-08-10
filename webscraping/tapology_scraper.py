#Tapology scraper I made to gather all of the mma gyms in MASS
import requests
import pandas as pd
from bs4 import BeautifulSoup

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

state_dfs = []

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
                gymname = row.text
                d["Name"] = gymname
                counter += 1
            elif counter == 1:
                location = row.text
                d["Location"] = location
                counter += 1
            elif counter == 2:
                phone = row.text
                d["Phone"] = phone
                counter +=1
            else:
                try:
                    site = row.find('a')
                    sitee = site.get('href')
                    d["Website"] = sitee
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




writer = pd.ExcelWriter('output.xlsx')
count = 0

for df in state_dfs:
    df.to_excel(writer,sheet_name=states[count], index=False)
    writer.save()
    count += 1
    
