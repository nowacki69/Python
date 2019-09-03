def my_func(a,  # This is the purpose of this variable
            b,  # This is the purpose of this variable
            c):
    print(a, b, c)

my_func(10, 
        20, 
        30)

my_func(10, # comment
        20, 
        30 # another comment
        )

a = [1, 2, 3]
print(a)

b = [1, 2,
    3, 4, 5]
print(b)

c = (1 #item 1
     , 2 #item 2
     , 3)
print(c)

d = {'key1': 1 #value for key 1
     ,'key2': 2 # value for key 2
     }
print(d)


a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
    
    print('yes')


a = '''this 
        is a string
        that is created over multiple lines
    '''
print(a)


def my_string():
    a = '''a multi-line string
that is indented in the second line'''
    return a

print(my_string())
