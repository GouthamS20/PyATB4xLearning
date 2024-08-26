# Program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

a = float(input("Enter the value of 1st side:"))
b = float(input("Enter the value of 2nd side:"))
c = float(input("Enter the value of 3rd side:"))

if a==b and b==c:
    print("It is an equilateral triangle")
elif a==b or a==c or b==c:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")

