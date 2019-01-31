from pyfiglet import figlet_format as fig
import requests
from random import randrange as rand

msg = "Dad Joke 3000"
title = fig(msg)
print(title)
print()

response = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"

if response == "":
    print("Here's a random joke:")
    res = requests.get(
        url,
        headers={"Accept":"application/json"}
    )
else:
    res = requests.get(
        url,
        headers={"Accept":"application/json"},
        params={'term': response}

    )

data = res.json()
jokes = data['results']

if len(jokes) > 1:
    if response != "":
        print(f"I've got {len(jokes)} about {response}. Here's one:")
    print(jokes[rand(1, len(jokes))]['joke'])
elif len(jokes) == 1:
    print(f"I've got a joke about {response}. Here it is:")
    print(jokes[0]['joke'])
else:
    print(f"I don't have any jokes about {response}. Try again...")
    
