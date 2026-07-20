# ==========================================================
# Question 25: Convert Days into Years, Months and Days
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# total number of days.
#
# Convert the given days into:
#
# • Years
# • Months
# • Remaining Days
#
# Assume:
#
# 1 Year = 365 Days
# 1 Month = 30 Days
#
# Example:
#
# Enter Total Days: 400
#
# -------------------------
# Years  : 1
# Months : 1
# Days   : 5
# ==========================================================
# ==========================================================

total_days = int(input("Enter Total Days: "))

years = total_days // 365

remaining_days = total_days % 365

months = remaining_days // 30

days = remaining_days % 30

print("-------------------------")
print("Years  :", years)
print("Months :", months)
print("Days   :", days)
print("-------------------------")