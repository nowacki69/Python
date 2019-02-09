from csv import reader, writer

def delete_users(filename, filename2, fname, lname):
    with open(filename) as input:
        csv_reader = reader(input)
        users = [user for user in csv_reader]

    deleted = 0
    with open(filename2, 'w') as output:
        csv_writer = writer(output)
        for user in users:
            if user[0] == fname and user[1] == lname:
                deleted += 1
            else:
                csv_writer.writerow(user)

        return f"Users deleted: {deleted}."

filename = "c:\\Users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users.csv"
filename2 = "c:\\Users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users2.csv"

print(delete_users(filename, filename2, "Wizard", "Nowacki"))       # Users deleted: 1.
print(delete_users(filename, filename2, "Cara", "Delevingne"))      # Users deleted: 2.
print(delete_users(filename, filename2, "Jessica", "Alba"))         # Users deleted: 0.
