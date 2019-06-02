import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='P0stgres69' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='P0stgres69' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='P0stgres69' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='P0stgres69' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='P0stgres69' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE tbl_store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
# insert("Wine Glass", 8, 10.5)
# insert("Water Glass", 10, 5)
# insert("Coffee Cup", 10, 5)
# delete("Coffee Cup")
# update(11, 6, "Water Glass")

# insert("Orange", 10, 15)
delete("Orange")
update(20, 15.0, "Apple")

print(view())
