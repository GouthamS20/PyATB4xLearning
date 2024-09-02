"""
Decorators
---------
A decorator is a special type of function that can modify or extend the behavior of another function.
It's a design pattern that allows you to wrap another function with additional functionality.

Helps to add logs to track automation scripts

It has many types

Type conversion
--------------
to convert the datatype of a variable
"""
import time


#Decorators
def add_before_ui_after_ui(custom_function_where_you_want_extra_func):
    # two parts
    # wrapper & call
    def wrapper():
        print("Before the running UI TC")
        print("Start the Browser ")
        custom_function_where_you_want_extra_func()
        print("Ending the running UI TC")
        print("Quit the Browser!")

    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will Test the UI")

#Checking the time taken by a function to execute
def time_check_decorator(func):
    def wrapper():
        stime = time.time()
        print(stime)
        func()
        etime = time.time()
        print(etime)
        print(f"The time taken is {etime - stime}")
    return wrapper()

@time_check_decorator
def test_ui_1():
    print("Time taken by func1")
    time.sleep(3)

#Type conversion
print(float(3))