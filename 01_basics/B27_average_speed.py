# ==========================================================
# Question 27: Calculate Average Speed
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Distance travelled
# • Time taken
#
# Calculate average speed using the formula:
#
# Speed = Distance / Time
#
# Display:
#
# • Distance
# • Time
# • Average Speed
#
# Example:
#
# Enter Distance: 150
# Enter Time: 3
#
# -------------------------
# Distance      : 150 km
# Time          : 3 hours
# Average Speed : 50 km/h
# ==========================================================


distance = float(input("Enter Distance: "))
time = float(input("Enter Time: "))

average_speed = distance / time

print("-------------------------")
print("Distance      :", distance, "km")
print("Time          :", time, "hours")
print("Average Speed :", average_speed, "km/h")
print("-------------------------")