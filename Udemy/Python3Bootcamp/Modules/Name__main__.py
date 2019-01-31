# to stop code from running if the code is not in the main app, add the following code:


def say_hi():
    print(f"Hi!  My __name__ is {__name__}")


if __name__ == "__main__":
    say_hi()
