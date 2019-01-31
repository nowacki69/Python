def display_info(a, b, *args, instructor = "Teacher", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name = "OfDaYear", job = "Instructor"))

# a = 1
# b = 2
# args (3, )
# instructor = "Teacher"
# kwargs = {'last_name':'OfDaYear', 'job':"Instructor"}
