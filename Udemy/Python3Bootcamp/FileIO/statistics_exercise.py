# Write a function called statistics, which takes in a file name and returns a dictionary with the nubmer of lines,
# words, and characters in the file.
def statistics(filename):
    results = dict.fromkeys(('lines','words','characters'), 0)
    with open(filename) as input:
        chapter = input.read()

    results['lines'] = chapter.count('\n') - 1
    results['words'] = chapter.count(' ') + results['lines']
    results['characters'] = len(chapter) - results['lines']

    return results

print(statistics("C:\\users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\story.txt"))
