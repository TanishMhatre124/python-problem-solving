# ==========================================================
# Question 5: Swap Two Variables Using a Temporary Variable
# ----------------------------------------------------------
# Create two variables:
#
# a = 10
# b = 20
#
# Print the values before swapping.
#
# Swap the values using a third variable named 'temp'.
#
# Print the values after swapping.
#
# Expected Output:
#
# Before Swapping
# a = 10
# b = 20
#
# After Swapping
# a = 20
# b = 10
# ==========================================================

a = 10
b = 20

print("Before Swapping")
print("a =", a)
print("b =", b)

temp=a
a=b
b=temp
print("after swapping")
print("a=",a)
print("b=",b)
