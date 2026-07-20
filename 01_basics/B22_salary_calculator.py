# ==========================================================
# Question 22: Calculate Total Salary
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Basic Salary
# • House Rent Allowance (HRA)
# • Travel Allowance (TA)
#
# Calculate the total salary:
#
# Total Salary = Basic Salary + HRA + TA
#
# Display:
#
# • Basic Salary
# • HRA
# • TA
# • Total Salary
# ==========================================================
# ==========================================================
# Question 22: Calculate Total Salary
# ==========================================================

basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter House Rent Allowance (HRA): "))
ta = float(input("Enter Travel Allowance (TA): "))

total_salary = basic_salary + hra + ta

print("-------------------------")
print("Basic Salary :", basic_salary)
print("HRA           :", hra)
print("TA            :", ta)
print("Total Salary  :", total_salary)
print("-------------------------")