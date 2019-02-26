# Now that we've learned about list methods, let's get some practice. See the problem statments in
# the comments below:

# Create a list called instructors
instructors=[]

# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
del instructors[0]

# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")

# Run the tests to make sure you've done this correctly!
print(instructors)
