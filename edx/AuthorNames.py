#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
# - There is no space or comma following the last period.
#
#Write a function called names_to_apa. names_to_apa should
#take as input one string, and return a reformatted string
#according to the style given above. You can assume that
#the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
#You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.


#Write your function below!
def names_to_apa(a_string):
    list_names = a_string.split(",")
    list_names[-1] = list_names[-1].replace(" and ", "")

    new_names = []
    
    for i in range(0, len(list_names)):
        list_names[i] = list_names[i].strip(" ")

    for name in list_names:
        fname, lname = name.split()
        new_names.append(lname + ", " + fname[0] + ".")

    newTitle = ""
    for i in range(0, len(list_names)):
        if i < (len(list_names) - 1):
            newTitle += new_names[i] + ", "
        else:
            newTitle += "& " + new_names[i]
            
    return newTitle

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("Walter Nowacki, First Last, David Joyner, and George Burdell"))


