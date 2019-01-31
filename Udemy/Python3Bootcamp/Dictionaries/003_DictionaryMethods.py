# Dictionary methods
# clear (clears all the entries in the dictionary)
cat2.clear()
print(cat2)

#copy (clones the dictionary)
cat2 = cat.copy()
print(cat2)

# fromkeys (usually used to create default values)
new_user = {}.fromkeys(['name','score','email','profile'], 'unknown')
print(new_user)
print()

#get
pet = cat.get('name')
print(pet)
home = cat.get('address')   # Does not error if non-existant
print(home)
print()



# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# Print out a string if food is in bakery_stock then print how many are left
# Print "We don't make that if it is not in bakery_stock.
print("Using IN")
if food in bakery_stock:
    print(f"We have {bakery_stock[food]} left of {food}")
else:
    print(food)
    print("We don't make that")

print("\nUsing get")
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
quantity = bakery_stock.get(food)
if quantity:
    print("{} left of {}".format(quantity, food))
else:
    print(food)
    print("we don't make that")

print()


#Fromkeys example
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)
print()


#pop (removes an item based on the key given)
initial_game_state.pop('ammo')
print(initial_game_state)
print()

#popitem (removes any random key from a dictionary)
initial_game_state.popitem()
print(initial_game_state)
print()

#update (updates the key and values in a dictionary)
newcatinfo = {'adopted':True, 'shots':True}

#to add the cat dictionary to the newcatinfo dictionary
newcatinfo.update(cat2)
print(newcatinfo)
print()


# Dictionary Methods Exercise
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')

print(stock_list)
