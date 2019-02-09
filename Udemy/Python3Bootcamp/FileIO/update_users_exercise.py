# update_users takes in an old first name, an old last name, a new first name, and a new last name. Updates the
# users.csv file so that any user whose first and last names match the old first and last names are updated to the new
# first and last names. The function should return a count of how many users were updated.

from csv import reader, writer

def update_users(filename, filename2, fname, lname, new_fname, new_lname):
    with open(filename) as input:
        csv_reader = reader(input)
        users = [user for user in csv_reader]

    updated = 0
    with open(filename2, 'w') as output:
        csv_writer = writer(output)
        for user in users:
            if user[0] == fname and user[1] == lname:
                csv_writer.writerow([new_fname, new_lname])
                updated += 1
            else:
                csv_writer.writerow(user)

        return f"Users updated: {updated}."

filename = "c:\\Users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users.csv"
filename2 = "c:\\Users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users2.csv"

print(update_users(filename, filename2, "Wizard", "Nowacki", "Hello", "World"))    # Users updated: 1.
# print(update_users(filename, filename2, "Jessica", "Alba", "Still not", "Here"))   # Users updated: 0.
# print(update_users(filename, filename2, "Dua", "Lipa", "Boba", "Fett"))            # Users updated: 2.
