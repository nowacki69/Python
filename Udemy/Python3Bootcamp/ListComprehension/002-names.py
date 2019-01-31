name = 'colt'
capped = [char.upper() for char in name]
print(capped)


friends = ['ashley', 'matt', 'michael']
capped2 = [friend[0].upper() for friend in friends]
print(capped2)


answer = [name[::-1].lower() for name in ["Elie", 'Tim', 'Matt']]
print(answer)
