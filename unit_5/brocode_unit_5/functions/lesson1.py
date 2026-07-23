# A function to display an invoice

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("BroCode", 42.49, "03 May 2026")



"""
In Python, .2f is a format specifier used to format a floating-point number to 
exactly two decimal places. It automatically rounds the number for display purposes without changing the original value.

Pro-Tip Adding Commas:
You can combine .2f with a comma to add a thousands separator for large numbers

balance = 1234567.891
print(f"Balance: ${balance:,.2f}")
# Output: Balance: $1,234,567.89
"""