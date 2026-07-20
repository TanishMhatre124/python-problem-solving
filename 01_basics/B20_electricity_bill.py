# ==========================================================
# Question 20: Electricity Bill Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Customer Name
# • Number of Units Consumed
# • Cost Per Unit
#
# Calculate the total electricity bill using:
#
# Bill = Units Consumed × Cost Per Unit
#
# Display:
#
# • Customer Name
# • Units Consumed
# • Cost Per Unit
# • Total Bill
#
# Example:
#
# Enter Customer Name: Tanish
# Enter Units Consumed: 150
# Enter Cost Per Unit: 8
#
# -------------------------
# Customer Name : Tanish
# Units Consumed : 150
# Cost Per Unit  : 8
# Total Bill     : 1200
# ==========================================================


# ==========================================================
# Question 20: Electricity Bill Calculator
# ==========================================================

customer_name = input("Enter Customer Name: ")

units_consumed = float(input("Enter Units Consumed: "))
cost_per_unit = float(input("Enter Cost Per Unit: "))

total_bill = units_consumed * cost_per_unit

print("-------------------------")
print("Customer Name :", customer_name)
print("Units Consumed:", units_consumed)
print("Cost Per Unit :", cost_per_unit)
print("Total Bill    :", total_bill)
print("-------------------------")