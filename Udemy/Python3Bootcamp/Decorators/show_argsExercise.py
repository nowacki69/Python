# Write a function called show_args which accepts a function and returns another function. Before invoking the function
# passed to it, show_args should be responsible for printing two things: a tuple of the positional arguments and a
# dictionary of the keyword arguments.
from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Here are the args: {args}")
        print(f"Here are the kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
