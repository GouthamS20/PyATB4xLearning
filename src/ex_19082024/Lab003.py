# Keywords and Identifiers
import keyword
print(keyword.kwlist)

#variable --> container and Identifiers
age = 56
print(age)
age = 67
print(age)

pi=3.14
_=22
_=_+1
name="Sample"
print(type(pi))
print(type(_))
print(type(name))
complex_number = 2+3j
print(complex_number.real)
print(complex_number.imag)
print(type(complex_number))

#Python is a dynamically typed language - data type of the variable can be changed at runtime

A = 10
B = 20
sum = A + B
sum = sum + 1
print(sum)
sum + 2 #InterviewTip: Here the value is only incremented but it is not being stored on the variable, to store is you need to assign it

