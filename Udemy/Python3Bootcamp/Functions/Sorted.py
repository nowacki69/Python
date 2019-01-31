numbers = [6,1,8,2]
new_numbers = sorted(numbers)
print(new_numbers)

new_numbers = sorted(numbers, reverse=True)
print(new_numbers)


users = [
    {"username":"samuel", 'tweets':['I love cake','I love pastries']},
    {'username':'katie', 'tweets':['I love my cat']},
    {'username':'jeff', 'tweets':[]},
    {'username':'bob', 'tweets':[]},
    {'username':'doggo_luvr', 'tweets':['dogs are the best']},
    {'username':'guitar_gal', 'tweets':[]},
]

print(sorted(users, key=lambda user: user['username']))
print()
print(sorted(users, key=lambda user: len(user['tweets'])))


print()
songs = [
    {'title':'happy birthday','playcount':1},
    {'title':'Survive','playcount':6},
    {'title':'YMCA','playcount':99},
    {'title':'Toxic','playcount':31}
]

print(sorted(songs, key=lambda s: s['playcount'], reverse=True))
