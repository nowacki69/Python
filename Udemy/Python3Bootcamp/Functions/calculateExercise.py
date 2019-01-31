def calculate(make_float, operation, first, second, message = ''):
    if operation == 'add': value = first + second
    if operation == 'subtract': value = first - second
    if operation == 'multiply': value = first * second
    if operation == 'divide': value = first / second

    if make_float == True:
        value = float(value)
    else:
        value = int(value)

    if message != '':
        msgTxt = message + " " + str(value)
    else:
        msgTxt = "The result is " + str(value)

    return msgTxt

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"
