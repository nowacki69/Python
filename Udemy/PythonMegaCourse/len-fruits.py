def GetFruits():
    myfile = open("fruits.txt", "r")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    myfile.close()
    for fruit in fruits:
        print(len(fruit))
    return 0

GetFruits()
