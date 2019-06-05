def GetFruits():
    myfile = open("fruits.txt", "r")
    fruits = myfile.read()
    myfile.close()
    return fruits

print(GetFruits())
