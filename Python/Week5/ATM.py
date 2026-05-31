# ################################################################
# #   PROBLEM 1: ATM SYSTEM
# ################################################################

# ----------------------------------------------------------------
# PROBLEM
# ----------------------------------------------------------------
# Build an ATM that keeps running until the user chooses to exit.
# Start with a balance of 1000 SAR.

# Show a main menu with these options:
#     1 - Show Balance
#     2 - Deposit
#     3 - Withdraw
#     0 - Exit

# Rules:
#   - The program must KEEP showing the menu after each
#     transaction.
# It only stops when the user chooses 0.

#   - Show Balance: print the current balance.
#   - Deposit: ask the user to choose an amount — 50, 100, 200,
#     or 500. Add it to the balance and show the new balance.
# The user can press 0 to cancel and go back to the menu.
# If they type an invalid amount, ask again.

#   - Withdraw: ask the user to choose an amount the same way.
# If the balance is enough, subtract it and show the new
#     balance. If not, show "Insufficient funds".
# The user can
#     press 0 to cancel. Invalid amounts ask again.
# Use loops so the application never exits until the user chooses
# 0 at each step.

# Solution: 
menu = """ 
1 - Show Balance
2 - Deposit
3 - Withdraw
0 - Exit
"""
balance = 1000
num = int (input("Enter your choice: "))

for i in menu:
    if num == "1":
       print ("balance")
print (menu)