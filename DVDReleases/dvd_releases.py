import os
import pandas as pd
import requests

from bs4 import BeautifulSoup
from datetime import datetime
from difflib import get_close_matches

# Get current folder path for csv files
cwd = os.getcwd()

# Get current year
now = datetime.now()
now.timetuple()
current_year = now.year

# set starting variables
start_year = 1990
base_url = "https://www.dvdsreleasedates.com/top-movies-"
collection = []

# *****************************************************************************
# Get previous years from storage (csv files), if they exist
# if they do not exist, retrieve data and save them

for year in range(start_year, current_year + 1, 1):
    filename = cwd + "\\" + str(year) + ".csv"

    # remove the current year's csv file in case anything has been updated.
    if year == current_year:
        try:
            os.remove(filename)
        except:
            pass

    # does the csv file exist for the selected year
    exists = os.path.isfile(filename)

    if exists:
        dfAll = pd.read_csv(filename)
    else:
        all_movies = []
        url = base_url + str(year) + "/"
        r = requests.get(url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        data = soup.find_all("td", {"class":"dvdcell"})
        for item in data:
            movie = {}
            # movie["Chart"] = str(year)
            movie["Position"] = int(list(item)[0])
            movie["Title"] = str(list(item)[4].string)

            try:
                movie["IMDB"] = float(item.find("td", {"class":"imdblink left"}).find("a").text)
            except:
                movie["IMDB"] = item.find("td", {"class":"imdblink left"}).find("a").text

            try:
                movie["Rating"] = item.find("td", {"class":"imdblink right"}).text.replace("\xa0", "")
            except:
                movie["Rating"] = None
            all_movies.append(movie)

        # Save the data to a CSV file by name of Year
        dfAll = pd.DataFrame(all_movies, columns=["Position", "Title", "IMDB", "Rating"])
        dfAll.to_csv(str(year) + ".csv", index=False, header=True)

    dfAll['Chart'] = str(year)
    collection.append(dfAll.values.tolist())
# /////////////////////////////////////////////////////////////////////////////

# *****************************************************************************
# Get list of movies I that I have
movie_dir = "E:\\Video\\_Movies\\"
my_movies = []
top_movies = []
have_movies = []
need_movies = []

# Create a list of all my movies
for dirName, subdirList, fileList in os.walk(movie_dir):
    for fname in fileList:
        my_movies.append(fname)

# Create a list of the top movie names
for y in collection:
    for movie in y:
        top_movies.append(movie)
        try:
            best_match = get_close_matches(movie[1], my_movies, 1)[0]
        except:
            need_movies.append(movie)
# /////////////////////////////////////////////////////////////////////////////

# Sort needed movies by ranked postion in each year
need_movies.sort(key=lambda x: x[0])

df = pd.DataFrame(need_movies, columns=['Rating', 'Title', 'IMDB', 'PG', 'Year'])
df.to_csv("MoviesNeeded.csv", index=False, header=True)
