# Your task is to write a function in the helpers.py file, and then call it
# from the this file. More specifically:
# 1. In helpers.py, define a function called lucky_number() that always returns
#    the number 37. That's it.
# 2. in this file, import the helpers module. In order for the testing logic
#    to work properly, don't use the 'as', or 'from' keywords when importing.
# 3. From inside this file, call the lucky_number function you defined in the
#    helpers module. Save the result to a variable called num.

import helpers

num = helpers.lucky_number()

print(num)
