import re

def is_valid_time(input):
    time_regex = re.compile(r'\d\d?:\d{2}')
    if time_regex.fullmatch(input) is not None:return True
    return False


print(is_valid_time("10:45"))   # True
print(is_valid_time("1:23"))    # True
print(is_valid_time("10.45"))   # False
print(is_valid_time("1999"))    # False
print(is_valid_time("145:23"))  # False
