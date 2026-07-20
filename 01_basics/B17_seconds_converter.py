# ==========================================================
# Question 17: Convert Seconds into Hours, Minutes and Seconds
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a time duration in seconds.
#
# Convert the given seconds into:
#
# • Hours
# • Minutes
# • Remaining Seconds
#
# Display all three values.
#
# Example:
#
# Enter Time in Seconds: 3665
#
# -------------------------
# Hours   : 1
# Minutes : 1
# Seconds : 5
#
# Hint:
# Use floor division (//) and modulo (%).
# ==========================================================

total_seconds=int(input("enter the time in seconds :"))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("hours:",hours)
print("minutes:",minutes)
print("seconds:",seconds)