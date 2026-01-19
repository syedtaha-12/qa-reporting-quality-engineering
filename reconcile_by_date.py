import sqlite3

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

# Source aggregates (validated layer)
cur.execute("""
SELECT
  date,
  COUNT(*) AS src_count,
  COALESCE(SUM(amount), 0) AS src_total
FROM transactions_validated
GROUP BY date
ORDER BY date;
""")
src_rows = cur.fetchall()

# Report aggregates (daily_summary)
cur.execute("""
SELECT
  date,
  transaction_count AS rpt_count,
  COALESCE(total_amount, 0) AS rpt_total
FROM daily_summary
ORDER BY date;
""")
rpt_rows = cur.fetchall()

conn.close()

# Convert results into dicts keyed by date
src = {d: (c, t) for (d, c, t) in src_rows}
rpt = {d: (c, t) for (d, c, t) in rpt_rows}

all_dates = sorted(set(src.keys()) | set(rpt.keys()))

print("=== Date-level Reconciliation ===")
all_pass = True

for d in all_dates:
    src_count, src_total = src.get(d, (0, 0))
    rpt_count, rpt_total = rpt.get(d, (0, 0))

    count_match = (src_count == rpt_count)
    total_match = (src_total == rpt_total)

    status = "PASS" if (count_match and total_match) else "FAIL"
    if status == "FAIL":
        all_pass = False

    print(f"\nDate: {d}")
    print(f"  Source (validated) -> count={src_count}, total={src_total}")
    print(f"  Report (summary)   -> count={rpt_count}, total={rpt_total}")
    print(f"  Status: {status}")

print("\n=== Overall Status ===")
print("REC-004 (By Date):", "PASS" if all_pass else "FAIL")
