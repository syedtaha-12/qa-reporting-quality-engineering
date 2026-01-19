# QA Checklist

- [x] Raw data ingested into transactions_raw
- [x] Validated layer created (filters null/negative amounts)
- [x] daily_summary generated from validated data
- [x] account_summary generated from validated data
- [x] Reconciliation PASS: totals and counts (validated vs daily_summary)
- [x] Reconciliation PASS: by date
- [x] Reconciliation PASS: by account
- [x] Reports exported: daily_summary_report.csv, account_summary_report.csv
