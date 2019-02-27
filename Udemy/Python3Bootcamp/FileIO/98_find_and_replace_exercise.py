# Write a function called find_and_replace which takes in a file name, a word to search for and a replacement word.
# Rplaces all instances of the word in the file with the replacment word.

def find_and_replace(filename, original, replacment):
    with open(filename) as input:
        contents = input.read()

    with open(filename, 'w') as output:
        contents = contents.replace(original, replacment)
        output.write(contents)

# find_and_replace("C:\\users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt",
#                     'Alice',
#                     'Jessica')

find_and_replace("C:\\users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt",
                    'Jessica',
                    'Alice')
