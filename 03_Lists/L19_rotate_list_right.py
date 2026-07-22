# ==========================================================
# Question L19: Rotate List to the Right
# ----------------------------------------------------------
# Write a Python program to rotate a list to the
# right by one position.
#
# Display:
#
# • Original List
# • Rotated List
#
# Example:
#
# Numbers: [10, 20, 30, 40, 50]
#
# -------------------------
# Original List : [10, 20, 30, 40, 50]
# Rotated List  : [50, 10, 20, 30, 40]
# -------------------------
# ==========================================================


numbers = [10, 20, 30, 40, 50]

rotated_list = [numbers[-1]] + numbers[:-1]

print("Original List :", numbers)
print("Rotated List  :", rotated_list)