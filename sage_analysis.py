import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files (using the correct column names from your output)
sales = pd.read_csv("sales_invoice_list.csv")
purchases = pd.read_csv("purchase_invoice_list.csv")

# ============================================
# Use the correct column names from your files
# ============================================
# Sales columns: 'Invoice Number', 'Invoice Date', 'Customer', 'Total', etc.
# Purchase columns: 'Invoice Date', 'Supplier', 'Total', etc.

# Use 'Total' column for both (as shown in your column lists)
sales_amount = sales["Total"].sum()
purchases_amount = purchases["Total"].sum()

total_income = sales_amount
total_expenses = purchases_amount
profit = total_income - total_expenses

# ============================================
# Print report
# ============================================
print("\n" + "="*50)
print("SAGE BUSINESS FINANCIAL SUMMARY")
print("="*50)
print(f"Total Income (Sales):     £{total_income:,.2f}")
print(f"Total Expenses (Purchases): £{total_expenses:,.2f}")
print(f"Profit:                   £{profit:,.2f}")
print("="*50)

# ============================================
# Create bar chart
# ============================================
categories = ["Income", "Expenses", "Profit"]
values = [total_income, total_expenses, profit]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=["green", "red", "blue"])
plt.title("Sage API Test Business - Financial Summary")
plt.ylabel("Amount (£)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("financial_summary.png")
print("\n✅ Chart saved as 'financial_summary.png'")

# ============================================
# Save to Excel report
# ============================================
with pd.ExcelWriter("sage_report.xlsx") as writer:
    sales.to_excel(writer, sheet_name="Sales Invoices", index=False)
    purchases.to_excel(writer, sheet_name="Purchase Invoices", index=False)
    
    summary = pd.DataFrame({
        "Metric": ["Total Income", "Total Expenses", "Profit"],
        "Amount (£)": [total_income, total_expenses, profit]
    })
    summary.to_excel(writer, sheet_name="Summary", index=False)

print("✅ Excel report saved as 'sage_report.xlsx'")
print("\n✅ Done! Files saved in your sage project folder.")
print("   Send these files to your teacher:")
print("   - sage_report.xlsx")
print("   - financial_summary.png")