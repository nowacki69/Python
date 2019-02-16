# 1 - Grabs data on every quote from the website http://quotes.toscrape.com
# 2 - You can use 'bs4' and 'requests' to get the data. For each quote you
#     should grab the 'text of the quote', the 'name of the person' who said
#     the quote, and the 'href of the link' to the person's bio. Store all of
#     this information in a list.

# 3 - Next, display the quote to the user and ask who said it. The player will
#     have four guesses remaining.

# 4 - After each incorrect guess, the number of guesses reamaining will
#     decrement.  If the player gets to zero guesses without identifying the
#     author, the player loses and the game ends.  If the player correctly
#     identifies the auther, the player wins!

# 5 - After every incorrect guess, the player receives a hint about the author.
#   a - For the first hint, make another request to the author's bio page (this
#       is why we originally scrape this data), and tell the player the
#       author's birth date and location.
#   b - The next two hints are up to you! Some ideas: the firt letter of the
#       author's first name, the first letter of the author's last name, the
#       number of letters in on of the names, etc.

# 6 - When the game is over, ask the player if they want to play again. If yes,
#     restart the game with a new quote. If no, the program is complete.
from bs4 import BeautifulSoup
from random import randint
import requests


def get_page():
    more_pages = True
    link = "http://quotes.toscrape.com"
    all_quotes = []
    page_num = 1

    while more_pages:
        if page_num == 1:
            full_url = link
        else:
            full_url = link + '/page/' + str(page_num) + '/'
        print(f"Scraping page {page_num}...")
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, "html.parser")

        next = soup.find("li", "next")
        if next is None:
            more_pages = False

        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            phrase = quote.find(class_="text").text
            author = quote.find(class_="author").text
            href = quote.find("a")['href']
            response2 = requests.get(link + href)
            soup2 = BeautifulSoup(response2.text, "html.parser")
            birth_date = soup2.find(class_="author-born-date").text
            birth_place = soup2.find(class_="author-born-location").text

            # print(author)
            all_quotes.append((author, phrase, birth_date, birth_place))
        page_num += 1
    return all_quotes


def get_quote(quotes):
    quotes_count = len(quotes)
    rand_index = randint(1, quotes_count) - 1

    author, phrase, birth_date, birth_place = quotes[rand_index][0:4]
    single_quote = ((author, phrase, birth_date, birth_place))
    return single_quote


def guess_quote(quote):
    print(quote[1])
    for x in range(4):
        guess = input(f"Who wrote this? Guesses remaining: {4 - x}. ")
        if guess == quote[0]:
            print("You guessed correctly! Congratulations!\n")
            return 0
        if x == 0:
            print(f"Here's a hint: The author was born on {quote[2]} in {quote[3]}\n")
        elif x == 1:
            print(f"Here's another hint: The first letter of the author's first name is '{quote[0][0]}'\n")
        elif x == 2:
            author = quote[0].split(" ")
            print(f"The first letter of the author's last name is '{author[1][0]}'\n")
        else:
            print(f"Sorry, you've run out of guesses. The answer was {quote[0]}\n")


print("Searching for quotes...")
complete_list_of_quotes = get_page()

play_again = True
while play_again:
    print("Here's a quote:\n")
    data = get_quote(complete_list_of_quotes)

    guess_quote(data)
    response = input("Would you like to play again (y/N)? ")
    if response != "y":
        play_again = False
        print("Ok! See you next time!")
