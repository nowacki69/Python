print(max(3,7,5,2))
print(min(3,7,5,2))


string = 'hello world'
print(max(string))
print(min(string))


names = ['Arya','Samson','Dora','Tim','Ollivander']
print(min(len(name) for name in names))

print(max(names, key=lambda name: len(name)))



songs = [
    {'title':'happy birthday','playcount':1},
    {'title':'Survive','playcount':6},
    {'title':'YMCA','playcount':99},
    {'title':'Toxic','playcount':31}
]
print(max(songs, key=lambda song: song['playcount'])['title'])
