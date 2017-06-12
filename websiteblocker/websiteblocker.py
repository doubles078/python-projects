#Script to block websites at certain times of the day
import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts.txt"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.reddit.com", "reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working hours.")
        with open(hosts_temp, 'r+') as file:
            content = file.read()

            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("Fun hours...")
    time.sleep(5)
