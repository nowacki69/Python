
# **var unpacks dictionaries

def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}

# display_names(first = "Rusty", second="Sue")
# display_names(names)      # nope..
display_names(**names)


def add_and_multiply(a,b,c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name='Tony')
add_and_multiply(**data, cat='blue')
