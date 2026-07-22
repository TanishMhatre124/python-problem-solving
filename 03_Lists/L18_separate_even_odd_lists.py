  # ==========================================================
# Question L18: Separate Even and Odd Numbers
# ----------------------------------------------------------
# Write a Python program to separate even and odd
# numbers into two different lists.
#
# Display:
#
# • Original List
# • Even Numbers List
# • Odd Numbers List
#
# Example:
#
# Numbers: [10, 15, 22, 33, 40, 51]
#
# -------------------------
# Original List     : [10, 15, 22, 33, 40, 51]
# Even Numbers      : [10, 22, 40]
# Odd Numbers       : [15, 33, 51]
# -------------------------
# ==========================================================


numbers= [10, 15, 22, 33, 40, 51]

even_number=[]
odd_number=[]

for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
    
    
    elif num % 2 !=0:
        odd_number.append(num)

print("Even Count : ",even_number)    
print("Odd Count : ",odd_number)