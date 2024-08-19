#Formatting is done to format the output
#Formatting Numbers
pi = 3.14159265357
formatted_pi = f"{pi:.4f}" #Prints 4 digits after the decimal point
print(formatted_pi)

#Format string using f-strings
num =88
print("The number you are working with is:"f"{num}")

#Print tables Eg: 9*1=9, 9*2=18, 9*3=27
tables = int(input("Enter the number you want the table to be printed:"))
print(f"{tables}*1={tables}") #value within the curly braces{} are actual values and values outside them are strings
print(f"{tables}*2={tables*2}")
print(f"{tables}*3={tables*3}")

#List Examples
ShoppingList=["Milk",'Panner',"Soda",1,23.4]
print(ShoppingList)
