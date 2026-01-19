import sqlite3

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

# Rebuild table each run for QA repeatability
cur.execute("DROP TABLE IF EXISTS account_summary;")

# Create account-level report from validated data
cur.execute("""
CREATE TABLE account_summary AS
SELECT
    account_id,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions_validated
GROUP BY account_id
ORDER BY account_id;
""")

conn.commit()

# Quick verification
cur.execute("SELECT * FROM account_summary;")
rows = cur.fetchall()

print("account_summary rows:")
for r in rows:
    print(r)

conn.close()
