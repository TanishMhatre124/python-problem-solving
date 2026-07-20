# ==========================================================
# Question 19: Percentage Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# marks obtained in five subjects.
#
# Assume each subject is out of 100 marks.
#
# Calculate:
#
# • Total Marks
# • Percentage
#
# Formula:
#
# Total Marks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
#
# Percentage = (Total Marks / 500) × 100
#
# Display:
#
# • Marks of all subjects
# • Total Marks
# • Percentage
#
# Example:
#
# Enter Subject 1 Marks: 80
# Enter Subject 2 Marks: 75
# Enter Subject 3 Marks: 90
# Enter Subject 4 Marks: 85
# Enter Subject 5 Marks: 70
#
# -------------------------
# Total Marks : 400 / 500
# Percentage  : 80%
# ==========================================================

# ==========================================================
# Question 19: Percentage Calculator
# ==========================================================

subject_1 = float(input("Enter Subject 1 Marks: "))
subject_2 = float(input("Enter Subject 2 Marks: "))
subject_3 = float(input("Enter Subject 3 Marks: "))
subject_4 = float(input("Enter Subject 4 Marks: "))
subject_5 = float(input("Enter Subject 5 Marks: "))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

percentage = (total_marks / 500) * 100

print("-------------------------")
print("Subject 1 Marks :", subject_1)
print("Subject 2 Marks :", subject_2)
print("Subject 3 Marks :", subject_3)
print("Subject 4 Marks :", subject_4)
print("Subject 5 Marks :", subject_5)
print("-------------------------")
print("Total Marks :", total_marks, "/ 500")
print("Percentage :", percentage, "%")