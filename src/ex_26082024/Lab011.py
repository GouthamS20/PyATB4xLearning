""""
Functions:
----------
defined using 'def' keyword followed by function name and parenthesis ()
two parts to a function --> definition & Calling
They may or may not return something.

_ and smaller cases i.e Snakecase are preferred by python while naming functions

order of execution of function depends on which is getting called first
"""

x = 10  # global variable

def my_function():
    x = 20  # local variable
    print(x)  # prints 20

print(x)
my_function()
