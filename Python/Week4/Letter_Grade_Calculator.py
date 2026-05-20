# Problem 1: Letter Grade Calculator
# ----------------------------------
# Ask the user for a score from 0 to 100 and print the letter grade:
#   - 90 to 100  -> A
#   - 80 to 89   -> B
#   - 70 to 79   -> C
#   - 60 to 69   -> D
#   - below 60   -> F
# Constraint: Do NOT use 'and'. Use the natural order of elif to
# handle the ranges.

#Solution:

score = int(input("Insert Your Score From (0-100): "))
if score > 100:
    print ("The Score Range is Between (0-100)")
else:
    if score >= 90:
        print ("A")
    elif score >= 80:
        print ("B")
    elif score >= 70:
        print ("C")
    elif score >= 60:
        print ("D")
    else:
        print ("F")
