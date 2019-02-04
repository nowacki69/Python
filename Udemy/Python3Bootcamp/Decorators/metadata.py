from functools import wraps
# wraps preserves a function's metadata
# when it is decorated

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y


print(add.__doc__)      # I AM WRAPPER FUNCTION
print(add.__name__)     # wrapper
help(add)               # wrapper(*args, **kwargs)
                        #    I AM WRAPPER FUNCTION
