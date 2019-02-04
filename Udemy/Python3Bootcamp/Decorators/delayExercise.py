# Write a function called delay which accpets a time and returns an inner
# function that accepts a function. When used as a decorator, delay will wait
# to execute the function being decorated by the amount of time passed into it.
# Before starting the timer, delay will also print a message informing the user
# that there will be a delay before the decorated function gets run.
from functools import wraps
from time import sleep

def delay(seconds):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds}s before running {fn.__name__}")
            sleep(seconds)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())

# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
