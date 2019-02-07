# add_user takes in a first name and a last name and adds a new user to the users.csv file

def add_user(first_name, last_name):
    from csv import DictWriter
    with open("c:\\users\\333051\\Documents\\Python\\Udemy\\\Python3Bootcamp\\FileIO\\users.csv", 'a') as oFile:
        headers = ["Last Name", "First Name"]
        csv_writer = DictWriter(oFile, fieldnames=headers)
        csv_writer.writerow({
            "First Name": first_name,
            "Last Name": last_name
        })

    return f"User ({last_name}, {first_name}) added..."

def get_name():
    for i in range(3):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        response = input (f"{first_name} {last_name} (y/n): ")
        if response.lower() == 'y':
            return add_user(first_name, last_name)

    return("Fucked up again...")

print(get_name())
