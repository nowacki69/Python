# Write a function called return_day. This function takes in one parameter (a number from 1-7) and
# returns the day of the week (1=Sunday, 2=Monday, ...). If the number is less than 1 or greater
# than 7, the function should return None

# Hint: stor the days of the week in a list (or dict using numbers as keys)
def return_day(num):
    days = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
    if num >0 and num < 8:
        return days[num]
    return None
    
print(return_day(2)) # "Monday"
print(return_day(1)) # "Sunday"
print(return_day(3)) # "Tuesday"
print(return_day(4)) # "Wednesday"
print(return_day(5)) # "Thursday"
print(return_day(6)) # "Friday"
print(return_day(7)) # "Saturday"
print(return_day(41)) # None
