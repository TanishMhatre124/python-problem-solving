# ==========================================================
# Question L14: Count Even and Odd Elements in a List
# ----------------------------------------------------------
# Write a Python program to count the number of even
# and odd elements in a list.
#
# Display:
#
# • Original List
# • Count of Even Numbers
# • Count of Odd Numbers
#
# Example:
#
# Numbers: [10, 15, 22, 33, 40, 51]
#
# -------------------------
# Original List      : [10, 15, 22, 33, 40, 51]
# Even Count         : 3
# Odd Count          : 3
# -------------------------
# ==========================================================

numbers= [10, 15, 22, 33, 40, 51]

even_number=0
odd_number=0

for num in numbers:
    if num % 2 == 0:
        even_number+=1
    
    
    elif num % 2 !=0:
        odd_number+=1

print("Even Count : ",even_number)    
print("Odd Count : ",odd_number)
