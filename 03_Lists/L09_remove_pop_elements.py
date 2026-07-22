 # ==========================================================
# Question L09: Remove and Pop Elements
# ----------------------------------------------------------
# Write a Python program that creates a list
# containing five fruits.
#
# Perform the following operations:
#
# • Remove "Banana" from the list
# • Remove the last element using pop()
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
# Updated List  : ['Apple', 'Mango', 'Orange']
# -------------------------
# ==========================================================

Fruits= ['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']
Fruits.remove("Banana")
Fruits.pop(-1)
print("Updated List  :",Fruits)