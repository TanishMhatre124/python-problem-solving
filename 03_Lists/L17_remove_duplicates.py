# ==========================================================
# Question L17: Remove Duplicate Elements from a List
# ----------------------------------------------------------
# Write a Python program to remove duplicate elements
# from a list without using set().
#
# Display:
#
# • Original List
# • List After Removing Duplicates
#
# Example:
#
# Numbers: [10, 20, 10, 30, 20, 40, 50, 40]
#
# -------------------------
# Original List            : [10, 20, 10, 30, 20, 40, 50, 40]
# Updated List             : [10, 20, 30, 40, 50]
# -------------------------
# ==========================================================



numbers = [10, 20, 10, 30, 20, 40, 50, 40]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original List :", numbers)
print("Updated List  :", unique)