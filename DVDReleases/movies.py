import os, re, requests
import pandas as pd

from datetime import datetime
from bs4 import BeautifulSoup


def remove_from_csv(mov):
    """
    mov should be a list with 5 elements:
        Rank, Title, IMDB, Rating, Year

    - opens the CSV file by year, finds the line that matches the movie data
    - removes that line from the list
    - save the data back to the CSV file

    """

    # Break the line into variables (mainly to get the year)
    rank, titl, imdb, rating, yr = mov
    # Format the data back into strings to write back to the CSV file
    mov = [rank, titl, imdb, rating]

    # Open the CSV file by year and get all lines into a list
    # with open(yr + '.csv', 'r') as csv_file:
    #     reader = csv.reader(csv_file)
    #     mov_list = list(reader)
    df1 = pd.read_csv(str(yr) + '.csv')
    mov_list = df1.values.tolist()

    # locate the specific movie in the list and remove it
    idx = mov_list.index(mov)
    mov_list.pop(idx)

    # Set the dataframe and save it to a CSV file (by Year)
    df1 = pd.DataFrame(mov_list, columns=["Position", "Title", "IMDB", "Rating"])
    df1.to_csv(str(yr) + '.csv', index=False, header=True)


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

        data = soup.find_all("td", {"class": "dvdcell"})
        for item in data:
            movie = {}
            # movie["Chart"] = str(year)
            movie["Position"] = int(list(item)[0])
            movie["Title"] = str(list(item)[4].string)

            try:
                movie["IMDB"] = float(item.find("td", {"class": "imdblink left"}).find("a").text)
            except:
                movie["IMDB"] = item.find("td", {"class": "imdblink left"}).find("a").text

            try:
                movie["Rating"] = item.find("td", {"class": "imdblink right"}).text.replace("\xa0", "")
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
need_movies = []

# Create a list of all my movies
for dirName, subdirList, fileList in os.walk(movie_dir):
    for fname in fileList:
        my_movies.append(fname)

my_movies.sort()

# Create a list of the top movie names
for y in collection:    # for every year
    for movie in y:     # for every movie
        top_movies.append(movie)
# /////////////////////////////////////////////////////////////////////////////

# *****************************************************************************
# Search for movie titles in my movies and remove them from the list
for movie in top_movies:
    title = re.sub(', The', '', movie[1])
    title = re.sub('The ', '', title)
    title = re.sub('[:.]', '', title)
    title.strip()

    for movi in my_movies:
        result1 = movi.find(title)
        result2 = movi.find(movie[4])
        older = str(int(movie[4])-1)
        result3 = movi.find(older)

        if result1 > -1 and (result2 > -1 or result3 > -1):
            try:
                index = top_movies.index(movie)
                del top_movies[index]
                remove_from_csv(movie)
            except:
                pass
# /////////////////////////////////////////////////////////////////////////////

# Sort remaining Top Movies by ranked postion in each year
# top_movies.sort(key=lambda x: x[0])

# Save the movies I don't have to a csv file
df = pd.DataFrame(top_movies, columns=['Ranking', 'Title', 'IMDB', 'Rating', 'Year'])
df.to_csv("MoviesNeeded.csv", index=None, header=True)
