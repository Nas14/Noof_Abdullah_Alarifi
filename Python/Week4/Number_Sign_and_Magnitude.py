# Problem 4: Number Sign and Magnitude
# ------------------------------------
# Ask the user for a number and print:
#   - "Negative large"  if the number is less than -100
#   - "Negative small"  if the number is between -100 and 0 (not 0)
#   - "Zero"            if the number is exactly 0
#   - "Positive small"  if the number is between 0 and 100 (not 0)
#   - "Positive large"  if the number is greater than 100
# Constraint: NO logical operators. Use ordered elif branches.

# Solution:

number = float(input("Enter a number: "))
if number < -100:
    print("Negative large")
elif -100 <= number < 0:
    print("Negative small")
elif number == 0:
    print("Zero")
elif 0 < number <= 100:
    print("Positive small")
else:
    print("Positive large")
