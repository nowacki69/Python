# Nested function
def outerFunction(text):
    def innerFunction():
        print(text)
    innerFunction()

outerFunction("Hello")

print('\n'+5)



# Closure Function
def outerFunction2(text):
    def innerFunction2():
        print(text)
    return innerFunction2

a = outerFunction2("Hello")
del outerFunction
# outerFunction("Hello")      # produces an error becuase it was deleted
print(a())

print('\n'+5)



def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of


square = nth_power(2)
print(square(3))
cube = nth_power(3)
print(cube(4))
