correct_password = "python123"
name = input("Enter Name: ")
surname = input("Enter Surname: ")
password = input("Enter Password: ")

while correct_password != password:
    print("Wrong password!")
    password = input("  Enter again: ")

message = "Hi %s %s, you are logged in" %(name, surname)
print(message)
