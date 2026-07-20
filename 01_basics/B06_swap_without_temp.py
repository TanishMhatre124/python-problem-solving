# ==========================================================
# Question 6: Swap Two Variables Without Using a Temporary
# Variable
# ----------------------------------------------------------
# Create two variables:
#
# a = 15
# b = 25
#
# Print the values before swapping.
#
# Swap the values without using any third variable.
#
# Do not create a variable named 'temp'.
#
# Print the values after swapping.
#
# Expected Output:
#
# Before Swapping
# a = 15
# b = 25
#
# After Swapping
# a = 25
# b = 15
# ==========================================================
a,b=10,20

print("Before Swapping")
print("a =", a)
print("b =", b)

a,b=b,a
print("after Swapping")
print("a =",a)
print("b =",b)

