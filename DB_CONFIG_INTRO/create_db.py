import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('site.db')

# Create a cursor
cursor = conn.cursor()

# Create table (use () instead of {})
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''') 

# Commit and close
conn.commit()
conn.close()

# Complex will use ORM instead