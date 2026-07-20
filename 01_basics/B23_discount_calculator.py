# ==========================================================
# Question 23: Discount Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Original Price
# • Discount Percentage
#
# Calculate:
#
# Discount Amount = (Original Price × Discount Percentage) / 100
#
# Final Price = Original Price - Discount Amount
#
# Display:
#
# • Original Price
# • Discount Percentage
# • Discount Amount
# • Final Price
#
# Example:
#
# Enter Original Price: 5000
# Enter Discount Percentage: 20
#
# -------------------------
# Original Price      : 5000
# Discount Percentage : 20%
# Discount Amount     : 1000
# Final Price         : 4000
# ==========================================================

original_price = float(input("Enter Original Price: "))
discount_percentage = float(input("Enter Discount Percentage: "))

discount_amount = (original_price * discount_percentage) / 100

final_price = original_price - discount_amount

print("-------------------------")
print("Original Price      :", original_price)
print("Discount Percentage :", discount_percentage, "%")
print("Discount Amount     :", discount_amount)
print("Final Price         :", final_price)
print("-------------------------")