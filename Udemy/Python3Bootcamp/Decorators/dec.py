def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Laura")

@be_polite
def rage():
    print("I hate you!")


# we are decorating our function with politeness
# greet = be_polite(greet)
greet()

# polite_rage = be_polite(rage)
rage()
