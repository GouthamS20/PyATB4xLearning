# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))
print("The maximum number is",max(num1,num2))
print("The power of num 1^num2",pow(num1,num2))
print("Sum:", num1+num2)
print("Difference:", num1-num2)
print("Product:", num1*num2)
print(f"Division: {(num1/num2):.2f}")
