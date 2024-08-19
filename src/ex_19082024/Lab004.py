"""
this is a multiline comment
"""
age=65
# = --> assignment operator (right to left)
#int, float are very large data types - Python automatically adjusts the value until it has memory

#Sample Math functions
a= pow(2,3)
b=abs (-7)
print(a,b)

#Taking input from the user
name = input("Enter your name please:")
print("Hi", name)
print(type(name)) #InterviewTip: Data type of 'input' is always a string

#Simple calculator program
num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:")) #Since input always takes a string value we are adding 'int' to convert it to an integer value
print("Sum:", num1+num2)
print("Difference:", num1-num2)
print("Product:", num1*num2)
print("Division:", num1/num2) #When two numbers are divided Python always returns a float value, this shows how python is superior when compared to other programming languages
