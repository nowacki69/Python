def find_user(fname, lname):
    from csv import DictReader
    user_file = "c:\\Users\\333051\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users.csv"
    with open(user_file) as users:
        index = 0
        userlist = DictReader(users)
        for user in userlist:
            if fname in user['First Name'] and lname in user['Last Name']: return index + 1
            index += 1
        return f"{fname} {lname} not found."

print(find_user("Cara", "Delevingne"))
print(find_user("Dua", "Lipa"))
print(find_user("Jessica", "Alba"))
