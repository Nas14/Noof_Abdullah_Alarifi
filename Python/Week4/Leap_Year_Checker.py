# Problem 2: Leap Year Checker
# ----------------------------
# A year is a leap year if:
#   - It is divisible by 4, AND
#   - It is NOT divisible by 100, UNLESS it is divisible by 400.
# Ask the user for a year and print "Leap Year" or "Not a Leap Year".
# Constraint: You may NOT use 'and' or 'or'. Use nested if statements.

# Solution:

year = int(input("Number of Years: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print (f"{year} is a Leap Year")
        else:
            print (f"{year} is Not a Leap Year")
    else:
        print (f"{year} is a Leap Year")
else:
    print (f"{year} is Not a Leap Year")
