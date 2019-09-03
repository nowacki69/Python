import pyodbc

# This line is used to test for existance of a valid MS Access Driver
# [print(x) for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Wizard\Documents\Python\AccessDB\access_db.accdb;')
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Wizard\Documents\Python\AccessDB\access_db.accdb;')
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()
cursor.execute('select * from names_table')

# This section will return all Table names
for table_info in cursor.tables(tableType='TABLE'):
    print(table_info.table_name)


# cursor.execute('''
#                     INSERT INTO names_table (First_Name, Last_Name, Age)
#                     VALUES('Cara', 'Delevingne',26)

#                   ''')


# cursor.execute('''
#                     INSERT INTO names_table (First_Name, Last_Name, Age)
#                     VALUES('Gigi', 'Hadid',24)

#                   ''')

# conn.commit()

cursor.execute("SELECT names_table.First_Name, names_table.Last_Name from names_table;")

results = cursor.fetchall()
for r in results:
    print(r)

cursor.close()
conn.close()
