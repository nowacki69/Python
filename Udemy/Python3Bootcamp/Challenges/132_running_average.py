# Create a function running_average that returns a function. When the function returned is passed a
# value, the function returns the current average of all previous function calls. You will have to
# use closure to solve this. You should round all answers to the 2nd decimal place.


def running_average():
    sum = 0
    count = 0
    def innerFunction(number):
        nonlocal sum                    # variable must be set as nonlocal if being modified in
        nonlocal count                  # innerFunction
        sum += number
        count += 1
        if count > 0: return sum/count  # must return SOMETHING
    return innerFunction                # return function with parentheses ALWAYS!!!


rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
