def string_length(mystring):
    if type(mystring) == int:
        print("Integers have no length")
    elif type(mystring) == float:
        print("Floats have no length")
    else:       
        print(len(mystring))

string_length("shit")
