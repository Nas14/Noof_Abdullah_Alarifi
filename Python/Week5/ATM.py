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
while True:
    print (menu)
    num = input("Enter your choice: ") 
    if not num.isdigit():
        print ("Please enter numbers only!")
        continue
    num = int(num)      
    if num == 1:
       print (f"The balance is: {balance} SAR")
    elif num ==  2:
        while True:
            deposit = int(input ("Enter an amout (50 - 100 - 200 - 500) or (0) to cancel: "))
            if deposit == 0:
                break
            elif deposit in [50,100,200,500]:
                balance += deposit
                print (f"Deposite Successfule!")
                print (f"The new balance is: {balance}SAR")
                
            else:
                print ("Invalid amount, Try again!")
    elif num == 3:
        while True:
            whithdrawl = int(input ("Enter an amout to withdrawl (50 - 100 - 200 - 500) or (0) to cancel: "))
            if whithdrawl == 0:
                break
            elif whithdrawl in [50,100,200,500]:
                if balance >= whithdrawl:
                    balance -= whithdrawl
                    print (f"Whithdrawl Successfule!")
                    print (f"The new balance is: {balance}SAR")
                else:
                    print ("Insufficient funds!")
                
            else:
                print ("Invalid amount, Try again!")
    elif num == 0:
        print ("Thank You!")
        break
    else:
        print ("Invalid Option Number! Try again!")