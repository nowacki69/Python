import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        w = w.lower()
        response = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? (y/n): ")
        if response == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif response != 'y':
            return "We could not find what you were looking for."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

definitions = (translate(word))
if type(definitions) == list:
    x = 1
    for definition in definitions:
        print(f"{x}: {definition}")
        x += 1
else:
    print(definitions)
