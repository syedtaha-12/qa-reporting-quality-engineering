import sqlite3

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

# List tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables:", tables)

# If transactions_raw exists, show row count
cur.execute("SELECT COUNT(*) FROM transactions_raw;")
print("transactions_raw row count:", cur.fetchone()[0])

conn.close()
