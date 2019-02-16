from functools import wraps

def decorator(function_to_decorate):
    @wraps(function_to_decorate)
    def wrapper(value):
        print(f"you are calling {function_to_decorate.__name__} with ’{value}’ as parameter")
        return function_to_decorate(value)
    return wrapper

@decorator
def replace_commas_with_spaces(value):
    return value.replace(",", " ")


print(replace_commas_with_spaces.__name__)      # wrapper
                                                # wraps changes this to 'replace_commas_with_spaces'
print(replace_commas_with_spaces.__module__)    # __main__
print(replace_commas_with_spaces.__doc__)       #None
print(replace_commas_with_spaces("my,commas,will,be,replaced,with,spaces"))
            # you are calling replace_commas_with_spaces with �my,commas,will,be,replaces,with,spaces� as parameter
            # my commas will be replaced with spaces
