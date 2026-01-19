import csv
import sqlite3

def count_csv_rows(path):
    with open(path, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # header
        return sum(1 for _ in reader)

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM daily_summary;")
db_daily = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM account_summary;")
db_acc = cur.fetchone()[0]

conn.close()

csv_daily = count_csv_rows("daily_summary_report.csv")
csv_acc = count_csv_rows("account_summary_report.csv")

print("DB daily_summary rows:", db_daily, "| CSV rows:", csv_daily)
print("DB account_summary rows:", db_acc, "| CSV rows:", csv_acc)

print("\nStatus:")
print("Daily export:", "PASS" if db_daily == csv_daily else "FAIL")
print("Account export:", "PASS" if db_acc == csv_acc else "FAIL")
