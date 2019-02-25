# Write a function called truncate that will shorten a string to a specified length, and add "..." to the end. Given a
# string and a number n, truncate the string to a shorter string containing at most n characters. For example,
# truncate("long string", 5) should return a 5 character truncated version of "long string". If the string gets
# truncated, the truncated return string should have a "..." at the end. Because of this, the smallest number passed
# in a second argument should be 3.

def truncate(string, length):
    if length < 3: return "Truncation must be at least 3 characters."
    if length > len(string) + 3: return string
    return string[0:length-3] + "..."


print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6)) # "Hel..."
print(truncate("Problem solving is the best!", 10)) # "Problem..."
print(truncate("Another test", 12)) # "Another t..."
print(truncate("Woah", 4)) # "W..."
print(truncate("Woah", 3)) # "..."
print(truncate("Yo",100)) # "Yo"
print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"
