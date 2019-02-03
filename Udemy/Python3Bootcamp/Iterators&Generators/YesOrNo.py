# Write a function called yes_or_no, which returns a generator that yields yes, then no, then yes, then no, and so on.
def yes_or_no():
    reply = "yes"
    while True:
        yield reply
        reply = "yes" if reply == "no" else "no"


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
