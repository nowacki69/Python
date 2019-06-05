numbers = [1,2,3]
myfile = open("numbers.txt","w")
for x in numbers:
    myfile.write(str(x) + "\n")
    
myfile.close()
