correct_password = "python123"
password = input("Enter Password: ")

while correct_password != password:
    print("Wrong password!")
    password = input("  Enter again: ")

print("Logged in")
