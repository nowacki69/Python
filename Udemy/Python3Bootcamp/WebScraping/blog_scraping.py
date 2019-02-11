# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("c:\\users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\WebScraping\\blog_data.csv", 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title",'url','date'])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
    