# ==========================================================
# Question 29: CAGR Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Initial Investment
# • Final Investment
# • Number of Years
#
# Calculate CAGR using:
#
# CAGR = ((Final / Initial) ** (1 / Years) - 1) × 100
#
# Display the CAGR percentage.
#
# Example:
#
# Initial Investment: 10000
# Final Investment: 15000
# Years: 5
#
# CAGR : 8.45%
# ==========================================================

# ==========================================================
# Question 29: CAGR Calculator
# ==========================================================

initial_investment = float(input("Enter Initial Investment: "))
final_investment = float(input("Enter Final Investment: "))
years = float(input("Enter Number of Years: "))

cagr = ((final_investment / initial_investment) ** (1 / years) - 1) * 100

print("-------------------------")
print("Initial Investment :", initial_investment)
print("Final Investment   :", final_investment)
print("Years              :", years)
print("CAGR               :", cagr, "%")
print("-------------------------")