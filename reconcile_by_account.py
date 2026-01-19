import sqlite3

conn = sqlite3.connect("banking_qa.db")
cur = conn.cursor()

# Source (validated layer)
cur.execute("""
SELECT
    account_id,
    COUNT(*) AS src_count,
    COALESCE(SUM(amount), 0) AS src_total
FROM transactions_validated
GROUP BY account_id
ORDER BY account_id;
""")
src_rows = cur.fetchall()

# Report (account_summary)
cur.execute("""
SELECT
    account_id,
    transaction_count AS rpt_count,
    COALESCE(total_amount, 0) AS rpt_total
FROM account_summary
ORDER BY account_id;
""")
rpt_rows = cur.fetchall()

conn.close()

src = {a: (c, t) for (a, c, t) in src_rows}
rpt = {a: (c, t) for (a, c, t) in rpt_rows}
all_accounts = sorted(set(src.keys()) | set(rpt.keys()))

print("=== Account-level Reconciliation ===")
all_pass = True

for acc in all_accounts:
    src_count, src_total = src.get(acc, (0, 0))
    rpt_count, rpt_total = rpt.get(acc, (0, 0))

    ok = (src_count == rpt_count) and (src_total == rpt_total)
    all_pass = all_pass and ok

    print(f"\nAccount: {acc}")
    print(f"  Source -> count={src_count}, total={src_total}")
    print(f"  Report -> count={rpt_count}, total={rpt_total}")
    print("  Status:", "PASS" if ok else "FAIL")

print("\n=== Overall Status ===")
print("REC-005 (By Account):", "PASS" if all_pass else "FAIL")

