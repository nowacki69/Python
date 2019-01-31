import sys
listComp = sys.getsizeof([x*10 for x in range(1000)])
genExp = sys.getsizeof(x*10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {listComp} bytes")
print(f"Generator Expression: {genExp} bytes")
