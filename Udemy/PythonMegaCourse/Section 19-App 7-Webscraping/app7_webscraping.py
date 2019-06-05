# import requests
import pandas

from bs4 import BeautifulSoup

with open(r"C:\Users\333051\Documents\Udemy\Python Mega Course\app7-webscraping\website\RockSprings.html") as file:

    r = file.read()

soup = BeautifulSoup(r, "html.parser")
# print(soup.prettify)

ALL = soup.find_all("div", {"class":"propertyRow"})

l=[]
for item in ALL:
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

    df = pandas.DataFrame(l)
    df.to_csv("Century.csv")


