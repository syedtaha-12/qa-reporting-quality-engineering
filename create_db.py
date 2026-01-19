import sqlite3
import csv

# 1. Create / connect to the SQLite database
conn = sqlite3.connect("banking_qa.db")
cursor = conn.cursor()

# 2. Create a table for raw transaction data
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions_raw (
    transaction_id INTEGER,
    account_id TEXT,
    amount REAL,
    date TEXT
)
""")

# 3. Load data from CSV into the database
with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
            INSERT INTO transactions_raw VALUES (?, ?, ?, ?)
        """, (
            int(row["transaction_id"]),
            row["account_id"],
            float(row["amount"]) if row["amount"] else None,
            row["date"]
        ))

# 4. Save changes and close the database connection
conn.commit()
conn.close()

print("Database created and data loaded successfully.")
