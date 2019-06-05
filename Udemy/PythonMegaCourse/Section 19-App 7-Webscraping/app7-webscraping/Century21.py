#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[19]:


# with open(r"C:\Users\333051\Documents\Udemy\Python Mega Course\app7-webscraping\website\RockSprings.html", 'r') as file:
#     r = file.read()


# In[38]:


l=[]

base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,30,10):
    r = requests.get(base_url + str(page) + ".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    print(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class":"propertyRow"})

    for item in all:
        d = {}
        d["Price"] = item.find("h4", {"class":"propPrice"}).text.replace("\n", "").replace(" ", "")
        d["Addresss"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
        d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text

        try:
            d["Beds"] = item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            d["Full Baths"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        try:
            d["Sq Ftg"] = item.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            d["Sq Ftg"] = None

        try:
            for column_group in item.find_all("div", {"class":"columnGroup"}):
                for feature_group, feature_name in zip(column_group.find_all("span", {"class","featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
                    if "Lot Size" in feature_group.text:
                        d["Lot Size"] = feature_name.text
        except:
            d["Lot Size"] = None

        l.append(d)    


# In[39]:


l


# In[40]:


import pandas
df = pandas.DataFrame(l)
df


# In[42]:


df.to_csv("Output.csv")

