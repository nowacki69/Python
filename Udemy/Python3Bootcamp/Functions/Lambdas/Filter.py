nums = [1,2,3,4]
print(list(filter(lambda x: x % 2 == 0, nums)))


names = ['austin','penny','anthony','angel','billy']
print(list(filter(lambda name: name[0]=='a', names)))



users = [
    {"username":"samuel", 'tweets':['I love cake','I love pastries']},
    {'username':'katie', 'tweets':['I love my cat']},
    {'username':'jeff', 'tweets':[]},
    {'username':'bob', 'tweets':[]},
    {'username':'doggo_luvr', 'tweets':['dogs are the best']},
    {'username':'guitar_gal', 'tweets':[]},
]

inactive_users = list(filter(lambda n: len(n['tweets']) == 0 ,users))

# Since and empty list is False, we can check if n['tweets'] is True or False
active_users = list(filter(lambda n: n['tweets'] ,users))

print(inactive_users)
print(active_users)
