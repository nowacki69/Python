import re
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result = pattern.sub("REDACTED", text)
print(result)

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result = pattern.sub("\g<1> REDACTED", text)
print(result)

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)
