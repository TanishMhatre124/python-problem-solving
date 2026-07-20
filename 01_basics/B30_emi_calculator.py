# ==========================================================
# Question 30: EMI Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Loan Amount
# • Annual Interest Rate
# • Loan Tenure in Years
#
# Calculate EMI using:
#
# EMI = P × r × (1+r)^n / ((1+r)^n - 1)
#
# Where:
#
# P = Loan Amount
# r = Monthly Interest Rate
# n = Number of Monthly Payments
#
# Display the Monthly EMI.
#
# Example:
#
# Loan Amount: 500000
# Interest Rate: 8
# Tenure: 5
#
# Monthly EMI : 10138.20
# ==========================================================

# ==========================================================
# Question 30: EMI Calculator
# ==========================================================

loan_amount = float(input("Enter Loan Amount: "))
annual_interest_rate = float(input("Enter Annual Interest Rate: "))
years = int(input("Enter Loan Tenure in Years: "))

monthly_interest_rate = annual_interest_rate / (12 * 100)

number_of_months = years * 12

emi = (loan_amount * monthly_interest_rate *
       (1 + monthly_interest_rate) ** number_of_months) / \
      (((1 + monthly_interest_rate) ** number_of_months) - 1)

print("-------------------------")
print("Loan Amount :", loan_amount)
print("Interest Rate :", annual_interest_rate, "%")
print("Tenure :", years, "Years")
print("Monthly EMI :", emi)
print("-------------------------")