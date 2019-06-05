# The code prints the output of the c_to_f  function multiple times in the terminal.
#
# For this exercise, write the output in a text file instead of printing the output in the terminal.
#
# The text file content will look like this:
#
# 50.0
# -4.0
# 212.0
#
# Don't write any message in the text file when input is lower than -273.15.


def save_file(temp):
    with open("temperatures.txt", "a") as tempfile:
        tempfile.write(str(temp) + '\n')

def c_to_f(c):
    if c < -273.15:
        print("That temperature doesn't make sense!")

    else:
        f = c* 9/5 + 32
        save_file(f)


temperatures = [10, -20, -289, 100]

for t in temperatures:
    c_to_f(t)
