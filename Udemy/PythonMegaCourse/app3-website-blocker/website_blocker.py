import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", 'facebook.com', 'msn.com', 'www.msn.com']

while True:
    if 6 < dt.now().hour < 15:
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"\n{redirect}    {website}")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
