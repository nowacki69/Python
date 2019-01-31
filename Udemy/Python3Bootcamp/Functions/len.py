print(len('asdasdas'))
print(len({'s':10, '10':'as'}))
print("Pennsylvania".__len__())


class SpecialList:
    def __init__(self, data):
        self.__data = data
    def __len__(self):
        return self.__data.__len__() // 2


l1 = SpecialList([1,40,30,100])
l2 = SpecialList([])

print(len(l1))
print(len(l2))
