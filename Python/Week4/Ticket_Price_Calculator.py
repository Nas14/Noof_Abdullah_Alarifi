# Problem 5: Ticket Price Calculator
# -----------------------------------
# A cinema charges tickets based on age and day:
#   - Age below 12         -> 20 SAR
#   - Age 12 to 17         -> 35 SAR
#   - Age 18 to 59         -> 50 SAR
#   - Age 60 or above      -> 25 SAR
# Additionally, on "Tuesday", every ticket gets a 10 SAR discount
# (minimum price must not go below 10 SAR).
# Ask the user for age and day, then print the final ticket price.
# Constraint: NO logical operators. Use nested conditions.

# Solution:

age = int(input("Enter your age: "))
day = input("Enter the day: ")
if age < 12:
    price = 11
elif age < 18:
    price = 35
elif age < 60:
    price = 50
else:
    price = 25
if day == "Tuesday":
    price = price - 10
    if price < 10:
        price = price + 10
    print ("No Discount Applied! Minimum price must not go below 10 SAR!")
print("Final ticket price:", price, "SAR")
