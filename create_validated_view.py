import sqlite3

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

cur.execute("""
CREATE VIEW IF NOT EXISTS transactions_validated AS
SELECT *
FROM transactions_raw
WHERE amount IS NOT NULL
  AND amount >= 0;
""")

conn.commit()

# Quick check
cur.execute("SELECT COUNT(*) FROM transactions_raw;")
raw_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM transactions_validated;")
valid_count = cur.fetchone()[0]

print("raw_count =", raw_count)
print("valid_count =", valid_count)

conn.close()
