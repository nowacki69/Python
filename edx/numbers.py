def load_file(data):
#    inputfile = open(filename, "r")
    
#    data = inputfile.readline()
#    inputfile.close()

    for value in data:
        value = value.strip()
        item = value.lstrip("-")
        item = item.replace(".", "")
        
        if item.isnumeric():
            if "." in value:
                item = float(value)
            else:
                item = int(value)
                
    return item

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
a_list = ["-9.32"]
contents = load_file(a_list)

print(contents)
print(type(contents))
