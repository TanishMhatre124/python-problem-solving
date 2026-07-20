# ==========================================================
# Question 14: Calculate Compound Interest
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Principal Amount
# • Rate of Interest (per year)
# • Time (in years)
#
# Calculate the Final Amount using the formula:
#
# Amount = Principal × (1 + Rate / 100) ** Time
#
# Then calculate the Compound Interest using:
#
# Compound Interest = Amount - Principal
#
# Display:
#
# Principal Amount
# Rate of Interest
# Time
# Final Amount
# Compound Interest
#
# Example:
#
# Enter Principal Amount: 10000
# Enter Rate of Interest: 10
# Enter Time: 2
#
# -----------------------------
# Principal Amount : 10000
# Rate             : 10%
# Time             : 2 years
# Final Amount     : 12100.0
# Compound Interest: 2100.0
# ==========================================================


principle_amount=float(input("enter the principle amount :"))
rate_of_interest=float(input("enter rate :"))
time=float(input("enter time :"))

final_amount = principle_amount * (1 + rate_of_interest / 100) ** time

compound_interest = final_amount - principle_amount

print("principle_amount :",principle_amount)
print("rate_of_interest :",rate_of_interest ,"%")
print("time :",time)
print("final amount:", final_amount)
print("compound interest",compound_interest)
