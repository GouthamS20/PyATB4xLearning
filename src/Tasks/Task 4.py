#Program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

import math

r = float(input("Enter the radius of the circle:"))
c_area = math.pi * r ** 2
print(f"The area of the circle is: {c_area:.3f}")
