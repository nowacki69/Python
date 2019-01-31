def sum_all_nums(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    return total

def sum_all_nums2(num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0):
    total = num1 + num2 + num3 + num4 + num5
    return total

# *args supplies the function with a tuple of values
def sum_all_nums3(num1, *args):
    print(num1)
    total = sum(args)
    return total

#print(sum_all_nums(4,6,9,4,10))
#print(sum_all_nums2(4,6))

print(sum_all_nums3(4,6,9,4,10))
print(sum_all_nums3(4,6))
