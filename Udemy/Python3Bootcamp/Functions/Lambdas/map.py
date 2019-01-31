# map
# A standard function that accepts at least two arguments, a function and an
# "iterable"
# once you iterate ove the value of a map, the map is then empty
# convert to a list for later use

nums = [2,4,6,8,10]

doubles = map(lambda x: x*2, nums)

for num in doubles: print(num)


people = ["Darcy", "Christina","Dana","Annabel"]
peeps = map(lambda name: name.upper(), people)
peeps = list(peeps)                    # convert to a list to save
print(peeps)


def triple(x): return x * 3
triples = list(map(triple, nums))
print(triples)
