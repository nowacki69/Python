import sqlite3
conn = sqlite3.connect(r"c:\Users\Wizard\Documents\Python\Udemy\Python3Bootcamp\sql\friends.db")
# create cursor object
c = conn.cursor()

people = [
	("Alina","Vicariu", 9),
	("Adriana", "Lima", 8),
	("Suzi", "Mickey", 7),
	("Brittany","Murphy", 7),
	("Kelly", "Hu", 3)]

# Insert all at once
# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)


# Insert while doing other calculations for actions
average = 0
for person in people:
	c.execute("INSERT INTO friends VALUES (?,?,?)", person)
	average += person[2]
print(average/len(people))


# commit changes
conn.commit()
conn.close()
