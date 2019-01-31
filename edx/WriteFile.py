def write_file(filename, data):
    openfile = open(filename, "w")
    openfile.write(str(data))
    openfile.close

write_file("c:\\temp\\WriteFileOutput.txt", 1301)
