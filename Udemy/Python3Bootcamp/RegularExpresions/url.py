import re

url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("http://www.youtube.com/videos/asd/das/asd")

print(match.group(0))   # http://www.youtube.com/videos/asd/das/asd
print(match.group(1))   # http
print(match.group(2))   # www.youtube.com
print(match.group(3))   # /videos/asd/das/asd
print()
print(f"Protocol: {match.group(1)}")
print(f"Base URL: {match.group(2)}")
print(f'Other(s): {match.group(3)}')
print()
print(match.groups())
