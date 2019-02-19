# Define a function called parse_date that accepts a single string. Your code should check to see if the string matches
# a date format. We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy" and
# "dd,mm,yyyy". If you are American, note that Day if before Month! However, rather than simply returning True or
# False if the string matches...you should instead return a dictionary containing the three parts of the date with the
# keys "d", "m", and "y" like so:

# Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None.
import re


def parse_date(string):
    date_regex = re.compile(r'(?P<d>\d\d)[\.|,|/](?P<m>\d\d)[\.|,|/](?P<y>\d{4})')
    match = date_regex.search(string)
    if match:
        day = match.group('d')
        month = match.group('m')
        year = match.group('y')
        if int(day) > 31 or int(month) > 12:
            return None
        else:
            return {'d': day,
                'm': month,
                'y': year
                }
    return None

print(parse_date("12,04,2003"))    # {'d':'12', 'm':'04', 'y':'1999'}
print(parse_date("12.11.2003"))    # {'d':'12', 'm':'11', 'y':'2003'}
print(parse_date("12.11.200312"))    # None
print(parse_date("01/22/1999"))    # {'d':'01', 'm':'22', 'y':'1999'}
