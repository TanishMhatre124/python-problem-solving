# ==========================================================
# Question L15: Linear Search in a List
# ----------------------------------------------------------
# Write a Python program to search for an element
# in a list without using the "in" operator.
#
# Display:
#
# • Original List
# • Search Element
# • Element Found or Not Found
#
# Example:
#
# Numbers: [10, 20, 30, 40, 50]
# Search Element: 30
#
# -------------------------
# Original List    : [10, 20, 30, 40, 50]
# Search Element   : 30
# Result           : Element Found
# -------------------------
# ==========================================================

numbers = [10,20,30,40,50]

search_element = int(input("Enter the number: "))

found = False

for num in numbers:
    if num == search_element:
        found = True

if found:
    print("Element Found")
else:
    print("Element Not Found")