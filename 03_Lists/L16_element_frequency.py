# ==========================================================
# Question L16: Count Frequency of an Element
# ----------------------------------------------------------
# Write a Python program to count how many times
# a given element appears in a list.
#
# Take the search element as input from the user.
#
# Display:
#
# • Original List
# • Search Element
# • Frequency
#
# Example:
#
# Numbers: [10, 20, 30, 20, 40, 20, 50]
# Search Element: 20
#
# -------------------------
# Original List    : [10, 20, 30, 20, 40, 20, 50]
# Search Element   : 20
# Frequency        : 3
# -------------------------
# ==========================================================

numbers=[10, 20, 30, 20, 40, 20, 50]
search_element = int(input("Enter the number: "))

count=0

for num in numbers:
    if num ==search_element:
        count+=1

print("search elements:",search_element)
print("frequency : ",count)


