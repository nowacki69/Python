# Write a function called parsing_bytes that accepts a single string. It should return a list of the binary bytes in
# the string. Each byte is just a combination of eight 1's or 0'sself.
import re

def parse_bytes(string):
    byte_regex = re.compile(r'\b[0-1]{8}\b')
    match = byte_regex.findall(string)
    return match

print(parse_bytes("11010101 101 323"))                 # ['11010101']
print(parse_bytes("my data is: 10101010 11100010"))    # ['10101010', '11100010']
print(parse_bytes("asdsa"))                            # []
