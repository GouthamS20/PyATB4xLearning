"""
List CRUD

Lambda function
--------------
lambda function is a small, anonymous function that can be defined inline within a larger expression. It's a shorthand way to create
a function without having to declare a separate named function
"""
my_shopping_list = ["milk","wheat","butter"]

def list_func(list):
    add_item = str(input("Enter an item:"))
    list.append(add_item)
    #list.remove(add_item)
    list.insert(1, add_item)
    return list

l = list_func(my_shopping_list)
print(l)

def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# find_odd_even(5)

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))

sums = lambda a,b: a+b
print(sums(1,2))