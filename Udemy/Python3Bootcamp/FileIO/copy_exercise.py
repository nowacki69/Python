# Write a function called copy, which takes in a file name and a new file name
# and copies the contents of the first file to the second file.

def copy(file, newFile):
    with open(file, 'r') as inFile:
        contents = inFile.read()
        with open(newFile, 'w') as outFile:
            outFile.write(contents)

# expects the contents of story.txt and story_copy.txt to be the same.
copy('C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt',
        'C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story_new.txt')
