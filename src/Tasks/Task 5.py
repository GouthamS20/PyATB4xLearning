#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the
#second number.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("num1 is greater" if num1 > num2 else "num2 is greater" if num2 > num1 else "num1 = num2")