# Write a function which accepts two parameters.  The function should return
# the # result of num1 divided by num2. If you do not pass the correct amount
# of arguments to the function, it should return the string 'Please provide two
# integers or floats'. If you pass as the 2nd argument a 0, Python will raise a
# ZeroDivisionError, so if this function is invoked with a 0 as the value of
# num2, return the string 'Please do not divide by zero'


def divide(num1, num2):
    try:
        value = num1 / num2

    except TypeError:
        return "Please provide two integers or floats"

    except ZeroDivisionError:
        return "Please do not divide by zero"

    else:
        return int(value)


# Examples
print(divide(4, 2))    # 2
print(divide([], "1"))  # "Please provide two integers or floats"
print(divide(1, 0))     # "Please do not divide by zero"
