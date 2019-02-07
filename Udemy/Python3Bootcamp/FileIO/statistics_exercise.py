# Write a function called statistics, which takes in a file name and returns a dictionary with the nubmer of lines,
# words, and characters in the file.
def statistics(filename):
    results = dict.fromkeys(('lines','words','characters'), 0)
    with open(filename) as input:
        lines = input.readlines()

    results['lines'] = len(lines)
    results['words'] = sum(len(line.split(' ')) for line in lines)
    results['characters'] = sum(len(line) for line in lines)
    return results

print(statistics("C:\\users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt"))
