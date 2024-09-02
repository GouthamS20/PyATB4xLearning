"""
Functions:
Functions in Python is a block of organized, reusable code that is used to perform a specific task.

1. Built-in
2. User defined

Types of user defined functions:
1. Function with no return type and no parameters
2. Function with no return type and with parameters
3. Function with no return type and with default parameters
4. Function with return type and with parameters

If we aren't sure how many parameters we need for a function we can use the following

*args is used to pass a non-keyworded, variable-length argument list to a function. It allows you to pass any number of
positional arguments as a tuple
**kwargs is used to pass a keyworded, variable-length argument dictionary to a function. It allows you to pass any number of
keyword arguments as a dictionary.

"""

#User defined function # with no return type and no parameters
def first_func():
    print("First function in python")

first_func()

#function with arguments but no return type
def greet_by_name(name):
    print("Hi",name)

greet_by_name("Jonathan") #Function arguments
greet_by_name(12345) #Any datatype can be passed as arguments

result = greet_by_name("Alice")
print(result) #Note: Print function doesn't return anything

#function with no return and default arguments:
def def_arg_example(n='Daniel'):
    print("Hey",n)

def_arg_example("John") #Positional argument
def_arg_example()
def_arg_example(n='Claire') #Keyword argument

#Function with arguments and return type
def func_with_arg_return_type(a,b):
    return a+b

r = func_with_arg_return_type(44,54)
print(r)

def my_function(*args, **kwargs):
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function('Hello', 'World', name='John', age=30)