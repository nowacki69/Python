# Write a function called repeat, which accepts a string and a number and returns a new string with the string passed
# to the function repeated the number amount of times. Do not use the built in repeat method!

def repeat(string, number):
    return string * number



print(repeat('*', 3)) # '***'
print(repeat('abc', 2)) # 'abcabc'
print(repeat('abc', 0)) # ''
