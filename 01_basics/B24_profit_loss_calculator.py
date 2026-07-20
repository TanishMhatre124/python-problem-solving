# ==========================================================
# Question 24: Profit or Loss Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Cost Price
# • Selling Price
#
# Calculate:
#
# Profit = Selling Price - Cost Price
#
# Loss = Cost Price - Selling Price
#
# Display the profit or loss amount.
#
# Note:
# For now, only calculate the value.
# Decision making using if-else will be covered later.
#
# Example:
#
# Enter Cost Price: 500
# Enter Selling Price: 700
#
# Profit Amount: 200
# ==========================================================

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

profit = selling_price - cost_price
loss = cost_price - selling_price

print("-------------------------")
print("Cost Price    :", cost_price)
print("Selling Price :", selling_price)

print("Profit Amount :", profit)
print("Loss Amount   :", loss)

print("-------------------------")