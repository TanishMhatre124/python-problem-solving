# ==========================================================
# Question L06: Modify List Elements
# ----------------------------------------------------------
# Write a Python program that creates a list
# containing five fruits.
#
# Perform the following operations:
#
# • Replace the second element with "Kiwi"
# • Replace the last element with "Pineapple"
#
# Display:
#
# • Original List
# • Updated List
#
# Example:
#
# Fruits: ['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']
#
# -------------------------
# Original List : ['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']
# Updated List  : ['Apple', 'Kiwi', 'Banana', 'Orange', 'Pineapple']
# -------------------------
# ==========================================================

Fruits=['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']
print("original list",Fruits)

Fruits[-1] = "Pineapple"
print("Updated List  :",Fruits)