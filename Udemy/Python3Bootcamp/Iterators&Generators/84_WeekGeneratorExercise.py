# Write a function called week, which returns a generator that yields each day of the week, starting with Monday and
# ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.

def week():
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for day in weekdays:
        yield day

days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
print(next(days)) # 'Wednesday'
print(next(days)) # 'Thursday'
print(next(days)) # 'Friday'
print(next(days)) # 'Saturday'
print(next(days)) # 'Sunday'
print(next(days)) # StopIteration
