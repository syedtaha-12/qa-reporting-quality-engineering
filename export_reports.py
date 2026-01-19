import sqlite3
import csv

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

# Export daily_summary
cur.execute("SELECT * FROM daily_summary;")
daily_rows = cur.fetchall()

with open("daily_summary_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "transaction_count", "total_amount"])
    writer.writerows(daily_rows)

# Export account_summary
cur.execute("SELECT * FROM account_summary;")
account_rows = cur.fetchall()

with open("account_summary_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["account_id", "transaction_count", "total_amount"])
    writer.writerows(account_rows)

conn.close()

print("Reports exported:")
print("- daily_summary_report.csv")
print("- account_summary_report.csv")
