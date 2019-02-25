import sqlite3
conn = sqlite3.connect(r"C:\Users\Wizard\Documents\Python\Udemy\Python3Bootcamp\SQL\\friends.db")

# create cursor object
c = conn.cursor()

# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
#                     VALUES ('Cara', 'Delevingne', 9)'''
# c.execute(insert_query)

# first = "Taylor"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (first,))

data = ("Taylor", "Swift", 8)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# commit changes
conn.commit()
conn.close()
