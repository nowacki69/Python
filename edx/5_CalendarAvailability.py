#Imagine you're writing a program to check if a person is
#available at a certain time.
#
#To do this, you want to write a function called
#check_availability. check_availability will have two
#parameters: a list of instances of the Meeting class, and
#proposed_time, a particular date and time.
#
#check_availability should return True (meaning the person
#is available) if there are no instances of Meeting that
#conflict with the proposed_time. In other words, it should
#return False if proposed_time is between the start_time and
#end_time for any meeting in the list of meetings.
#
#The Meeting class is defined below. It has two attributes:
#start_time and end_time. start_time is an instance of the
#datetime class showing when the meeting starts, and
#end_time is an instance of the datetime class indicating
#when the meeting ends.
#
#Hint: Instances of the datetime have at least six
#attributes: year, month, day, hour, minute, and second.
#
#Hint 2: Comparison operators work with instances of the
#datetime class. time_1 < time_2 will be True if time_1 is
#earlier than time_2, and False otherwise.
#
#You should not assume that the list is sorted.

#Here is our definition of the Meeting class:
from datetime import datetime
class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

#Write your function here!
def check_availability(meetingList, rTime):
    Available = True
    for i in range(len(meetingList)):
        if rTime >= meetingList[i].start_time and rTime < meetingList[i].end_time:
            return False

    return Available



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
meetings = [Meeting(datetime(2018, 8, 4, 12, 0, 0), datetime(2018, 8, 4, 14, 0, 0)),
            Meeting(datetime(2018, 8, 7, 14, 45, 0), datetime(2018, 8, 7, 16, 45, 0)),
            Meeting(datetime(2018, 8, 4, 16, 45, 0), datetime(2018, 8, 4, 18, 15, 0)),
            Meeting(datetime(2018, 8, 5, 12, 0, 0), datetime(2018, 8, 5, 13, 30, 0)),
            Meeting(datetime(2018, 8, 3, 15, 0, 0), datetime(2018, 8, 3, 16, 15, 0)),
            Meeting(datetime(2018, 8, 7, 16, 0, 0), datetime(2018, 8, 7, 16, 45, 0)),
            Meeting(datetime(2018, 8, 6, 16, 0, 0), datetime(2018, 8, 6, 17, 45, 0)),
            Meeting(datetime(2018, 8, 5, 16, 0, 0), datetime(2018, 8, 5, 18, 30, 0))]

print(check_availability(meetings, datetime(2018, 8, 7, 16, 30, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))


