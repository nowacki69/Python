# Write a function called copy_and_reverse which takes in a file name and a new file name and copies the reversed
# contents of the first file to the second file.


# This function reads the entire file into a list of strings, reverses the list, then reverses each string in the list
def copy_and_reverse(file, newFile):
    with open(file) as input:
        chapter = input.readlines()

        with open(newFile, 'w') as output:
            for line in chapter[-1::-1]:
                for char in line[-1::-1]:
                    output.write(char)


#
#    OR
#


# This function takes the entire file in as a single string, then reverses that string.
def c_and_r(file, newFile):
    with open(file) as inFile:
        txt = inFile.read()

    with open(newFile, 'w') as outFile:
        outFile.write(txt[::-1])

copy_and_reverse("C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt",
                    "C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story_reversed.txt")

c_and_r("C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt",
                    "C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story_reversed2.txt")
