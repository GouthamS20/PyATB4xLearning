"""
Match:
Same as switch in C++
match statement in Python 3.10 and greater is a powerful feature that allows you to control program flow using pattern matching.

No break statement is needed unlike other languages
"""

#Program to ask user to use which browser to execute an automation script

b_name = input("Enter the Browser:")
match b_name:
    case "firefox":
        print("Executing in firefox")
    case "chrome":
        print("Executing in Chrome")
    case "safari":
        print("Executing in Safari")
    case "edge":
        print("Executing in Edge")
    case _:
        print("Browser not found")