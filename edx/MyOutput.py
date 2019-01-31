string1 = "Hi!"
string2 = "Hey!"
string3 = "Hello!"

outputFile = open("c:\\temp\\MyOutput.txt", "w")
outputFile.write(string1 + "\n")
outputFile.write(string2 + "\n")
outputFile.write(string3 + "\n")
outputFile.close()
