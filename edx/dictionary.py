def tup_to_dict(tupleList):
    myDict = {}
    for pair in tupleList:
        myDict[pair[0]] = pair[1]
    
    return myDict


print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))

