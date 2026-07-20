# ==========================================================
# Question 10: Calculate the Perimeter of a Rectangle
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# the length and breadth of a rectangle.
#
# Calculate the perimeter of the rectangle using
# the formula:
#
# Perimeter = 2 × (Length + Breadth)
#
# Display the calculated perimeter in a clear and
# readable format.
#
# Example:
#
# Enter length : 10
# Enter breadth: 5
#
# Perimeter = 30
# ==========================================================


length=float(input("enter length :"))
breadth=float(input("enter breadth:"))

perimeter=2*(length+breadth)

print("perimeter =", perimeter)