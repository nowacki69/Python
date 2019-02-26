# I've written some code at the top of the file for you. Please don't touch it, if you'd like the
# tests to work :)  All the code does is randomly set the food variable to either 'apple','grape',
# 'bacon','steak', or 'dirt'. Don't worry about how it works for now, we'll learn more shortlyself.

# When you run the prewritten code, food will be randomly assigned. Your task is to write code that
# will classify what the food isself.
#   * If food is set to either 'apple' or 'grape', your code should print 'fruit'.
#   * If food is set to either 'bacon' or 'steak', your code should print 'meat'.
#   * If food is set to either 'dirt' or 'worm', your code should print 'yuck'.

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food is 'apple' or food is 'grape':
    print('fruit')
elif food is 'bacon' or food is 'steak':
    print('meat')
elif food is 'dirt' or food is 'worm':
    print('yuck')
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
