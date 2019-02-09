def print_users(filename):
    from csv import DictReader
    with open(filename, 'r') as iFile:
        csv_reader = DictReader(iFile)
        for row in csv_reader:
            print(f"{row['First Name']} {row['Last Name']}")

file_name = "c:\\Users\\Wizard\\Documents\\Python\\Udemy\\Python3Bootcamp\\FileIO\\users.csv"
print_users(file_name)
