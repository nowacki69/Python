# Write a function called double_return which accepts a function and returns another function.
# double_return should decorate a function by returning two copies of the innerfunction's return value inside of a list
from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, *kwargs)
        return [result, result]
    return wrapper


@double_return
def add(x, y):
    return x + y


@double_return
def greet(name):
    return "Hi, I'm " + name


print(add(1, 2)) # [3, 3]
print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]
