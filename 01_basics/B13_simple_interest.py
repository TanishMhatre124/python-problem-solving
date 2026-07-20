# ==========================================================
# Question 13: Calculate Simple Interest
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Principal Amount
# • Rate of Interest (per year)
# • Time (in years)
#
# Calculate the Simple Interest using the formula:
#
# Simple Interest = (Principal × Rate × Time) / 100
#
# Display:
#
# • Principal Amount
# • Rate of Interest
# • Time
# • Simple Interest
#
# Example:
#
# Enter Principal Amount: 10000
# Enter Rate: 8
# Enter Time: 2
#
# Simple Interest = 1600
# ==========================================================

principle_amount=float(input("enter the principle amount :"))
rate_of_interest=float(input("enter rate :"))
time=float(input("enter time :"))

simple_interest=(principle_amount*rate_of_interest*time)/100

print("simpple interst :", simple_interest)
print("principle_amount :",principle_amount)
print("rate_of_interest :",rate_of_interest ,"%")
print("time :",time)