# ==========================================================
# Question L20: Merge Two Lists
# ----------------------------------------------------------
# Write a Python program to merge two lists into
# a single list without using extend().
#
# Display:
#
# • First List
# • Second List
# • Merged List
#
# Example:
#
# List 1: [10, 20, 30]
# List 2: [40, 50, 60]
#
# -------------------------
# First List   : [10, 20, 30]
# Second List  : [40, 50, 60]
# Merged List  : [10, 20, 30, 40, 50, 60]
# -------------------------
# ==========================================================

List_1= [10, 20, 30]
List_2=[40, 50, 60]

merged_list=[]

for num in List_1:
    merged_list.append(num)

for num in List_2:
    merged_list.append(num)
print(merged_list)