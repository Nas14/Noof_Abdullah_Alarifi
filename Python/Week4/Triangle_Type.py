# Problem 3: Triangle Type
# ------------------------
# Ask the user for the three sides of a triangle (a, b, c). Print:
#   - "Equilateral" if all three sides are equal.
#   - "Isosceles"   if exactly two sides are equal.
#   - "Scalene"     if no sides are equal.
# Constraint: NO logical operators. Use nested if-else.

# Solution:

triangle1 = int(input("Insert Side (a):"))
triangle2 = int(input("Insert Side (b):"))
triangle3 = int(input("Insert Side (c):"))
if triangle1 == triangle2 == triangle3:
    print ("The Triangle is Equilateral")
elif triangle1 == triangle2 != triangle3:
    print ("The Triangle is Isosceles")
elif triangle1 != triangle2 == triangle3:
    print ("The Triangle is Isosceles")
elif triangle1 == triangle3 != triangle2:
    print ("The Triangle is Isosceles")
else:
    print ("The Triangle is Scalene")


