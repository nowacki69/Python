import sqlite3
conn = sqlite3.connect(r"C:\Users\Wizard\Documents\Python\Udemy\Python3Bootcamp\SQL\friends.db")

# create cursor object
c = conn.cursor()
# c.execute("SELECT * FROM friends WHERE first_name IS 'Cara'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness DESC")


# Iterate over cursor
# for result in c:
# 	print(result)

# Fetch One Result
# print(c.fetchone())

# Fetch all results as list
print(c.fetchall())


# commit changes
conn.commit()
conn.close()
