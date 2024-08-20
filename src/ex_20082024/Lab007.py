#There are new data types being added in python

#decimal literal --> base 10
a = 25

#Binary literals --> base 2
binary_number = 0b1010 #0's and 1's after 0b digit indicates the binary number
#Similarly we have Octal, hexadecimal

#Escape sequence --> these are literals as well
print("Hi\nSoldiers")

#raw(string) --> Use case: You want to indicate a file path in your program which may contain escape sequences
#Note: Used for API Automation, Web Automation,file_path = r concept
dirct = r"C:\Goutham\n.txt"
print(dirct)

#Ternary operator in Python
print("You can vote" if int(input('Enter age:')) >=18 else "You can't vote")


