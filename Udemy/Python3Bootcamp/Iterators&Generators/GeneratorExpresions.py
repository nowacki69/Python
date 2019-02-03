def nums():
    for num in range(1, 10):
        yield num


g = nums()
print(next(g))
print(next(g))
print(next(g))

g2 = (num for num in range(1, 10))
print(next(g2))
print(next(g2))
print(next(g2))

l = [num for num in range(1,10)]
print(l)

print([sum(num for num in range(1, 10))])
print(sum(num for num in range(1, 10)))


import time
gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_stop_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_stop_time = time.time() - list_start_time

print(f"The 100mil generator range took: {gen_stop_time}")
print(f"The 100mil list range took: {list_stop_time}")
