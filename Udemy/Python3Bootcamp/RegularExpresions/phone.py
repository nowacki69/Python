import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    else:
        return None


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


def is_valid_phone(input):
    # phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    # match = phone_regex.search(input)
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return match.group()
    else:
        return None

print(extract_phone("my number is 412 969-7706 or call me at 412 715-8675"))
print(extract_phone("my number is 412 969-770656"))
print(extract_phone("412 969-7706 is my number"))
print(extract_phone("412 969-7706"))

print(extract_all_phones("my number is 412 969-7706 or call me at 412 715-8675"))
print(extract_all_phones("my number is 412 969-770656"))
print(extract_all_phones("412 969-7706 is my number"))
print(extract_all_phones("412 969 7706"))

print(is_valid_phone("my number is 412 969-7706 or call me at 412 715-8675"))
print(is_valid_phone("my number is 412 969-770656"))
print(is_valid_phone("412 969-7706 is my number"))
print(is_valid_phone("412 969-7706"))
