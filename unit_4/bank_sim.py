"""
The Challenge: The Smart ATM Withdrawal Simulator
*description*: simulate a bank transaction checking if a user has enough money
"""
print("=" * 30)
print("WELCOME TO THE SMART FNB ATM")
print("=" * 30)

# 1. Set fixed variable for bank balance
balance = 500
print(f"your current balance is: R{balance}")
print('-' * 30)

# 2. Ask user how much they want to withdraw
withdrawal_amount = int(input("How much would you like to withdraw?: R"))

if withdrawal_amount <= balance and withdrawal_amount > 0:
    balance = balance - withdrawal_amount
    print(f'Withdrawal successful! Remaining balance is: R{balance}')
elif withdrawal_amount < 0 or withdrawal_amount == 0:
    print("Invalide amount: You must withdraw more than R0")
else:
    print("Declined. Insufficient funds")