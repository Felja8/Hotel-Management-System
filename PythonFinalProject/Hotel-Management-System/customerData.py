import sqlite3

conn = sqlite3.connect('guest_data_base.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS guests (
          firstname TEXT,
          country TEXT,
          passport TEXT,
          gender TEXT,
          from_date TEXT,
          to_date TEXT
)""")  
conn.commit()

c.execute("SELECT name FROM sqlite_master WHERE type='table'")

tables = c.fetchall()
for table in tables:
    print(table[0])

c.execute("SELECT * FROM guests")

# Fetch all rows from the query
rows = c.fetchall()

# Check if the table has data
if rows:
    # Print the column headers
    print("firstname, country, passport, gender, from_date, to_date")
    
    # Print each row of data
    for row in rows:
        print(", ".join(map(str, row)))
else:
    print("No data found in the 'guests' table.")
conn.close()