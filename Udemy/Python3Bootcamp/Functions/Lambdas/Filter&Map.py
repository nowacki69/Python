names = ['Lassie','Colt','Rusty']

five_or_less = list(map(lambda name: f"Your instructor is {name}",
                    filter(lambda value: len(value) < 5, names)))

print(five_or_less)



users = [
    {"username":"samuel", 'tweets':['I love cake','I love pastries']},
    {'username':'katie', 'tweets':['I love my cat']},
    {'username':'jeff', 'tweets':[]},
    {'username':'bob', 'tweets':[]},
    {'username':'doggo_luvr', 'tweets':['dogs are the best']},
    {'username':'guitar_gal', 'tweets':[]},
]

usernames = list(map(lambda user: user["username"],
    filter(lambda u: not u['tweets'], users)))
print(usernames)
print()

# Using List Comprehension instead...
print([user['username'] for user in users if not user['tweets']])
