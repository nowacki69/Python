# Zip - make an iterator that aggregates elements from each of the iterables
#     - returnse an iterator of tuples, wehre the -eth tuple contains the i-th
#       element from each of the argument sequences or iterables

nums = [1,2,3,4,5]
chars = ['a','b','c','d','e']
symbols = ["!","@","#","$","%"]

nList = zip(nums, chars, symbols)
print(list(nList))
print()



midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

# get the student and thier highest grade
# final_grades = [max(grades) for grades in zip(midterms, finals)]
final_grades = {grades[0]:max(grades[1], grades[2]) for grades in zip(students,
                midterms, finals)}
print(final_grades)
print()

final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)
print("Final Grades:")
print(final_grades)
print()
print("Average Grades")
print(avg_grades)
