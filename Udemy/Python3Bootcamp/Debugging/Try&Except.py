def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {'name':'Ricky'}
print(get(d, 'name'))
print(get(d, 'city'))


while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:      # runs if a ValueError occurs
        print("That's not a number!")
    else:                   # runs after success of the try statement
        print("Good job, you entered a number.")
        break
    finally:                # runs if there is an error or not.
        print("This runs at the end, no matter what happens.")
