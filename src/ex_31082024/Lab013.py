"""
Functions contd:
---------------
def(*t,*v): --> this is not possible
def(t,*v): --> this is incorrect, *args should always be at the first


Scope:
-----
scoping refers to the rules that govern how variables are accessed and resolved within a program. There are two main types of
scoping in Python: Local Scoping and Global Scoping.

In Python, local variables have a higher preference than global variables. This means that when you assign a value to a variable
within a function or a block, Python will create a local variable with that name, even if a global variable with the same name
exists.

Nonlocal Scoping (Python 3.x only):
Nonlocal scoping is a new feature introduced in Python 3.x. It allows a function to access variables from an outer scope, but not
from the global scope.
"""
gbv = 20 #works like a global variable (scope is throughout the entire program)

def make_pizza(*toppings,base):
    print(toppings,base)

make_pizza("Chicken",'mushroom','veggies',base='wheat')

#Scope
def scope_eg():
    a= 10
    print(a) #local variable (scope is within the function)
    print(gbv)

scope_eg()
print(gbv)

def scope_eg2():
    global gbv #use 'global' keyword within the function to directly update the global variable
    gbv=50
    print(gbv)

scope_eg2()

def outer():
    x = 10  # nonlocal variable

    def inner():
        nonlocal x  # access x from outer scope
        print(x)  # prints 20

    inner()
    print(x)  # prints 20

outer()