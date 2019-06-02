def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless"
    except:
        return "Another error occurred"


print(divide(1,0))
print(divide(1,'a'))
print(divide(1,1))
