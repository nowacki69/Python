# import regex module
import re

# define our phone numberregex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a strin with our regex
res = pattern.findall('Call me at 412 969-7706 or 412 537-9252')

for match in res:
    print(match)
