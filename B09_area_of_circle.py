# ==========================================================
# Question 9: Calculate the Area of a Circle
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# the radius of a circle.
#
# Calculate the area of the circle using the formula:
#
# Area = π × Radius × Radius
#
# You may use:
#
# • 3.14 as the value of π
# OR
# • math.pi from Python's math module.
#
# Display the calculated area in a clear and
# readable format.
#
# Example:
#
# Enter radius: 7
#
# Area = 153.94
# ==========================================================

radius=float(input("enter length :"))
area=3.14*radius*radius

print("area of circle",area)