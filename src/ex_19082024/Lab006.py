#String Manipulation
a=90 #dataype is int
b=90
a="90" #datatype is string

name="Google"
print(name.upper())
print(len(name)) #String length

#name=name+1; #TypeError: can only concatenate str (not "int") to str
name=name+str(1) #String Concatenation
print(name)

#None datatype
planes_i_own = None
print(type(planes_i_own)) #There is nothing called as 'null' datatype in python

#id - Address/Memory location -->used in API automation
print(id(a)) #2664277594864
print(id(b)) #Suppose you store two variables with the same value say a=10 and b=10 then python somtimes points to the same memeory location to avoid space issue
#but if it takes a different value then a separate memory is allocated
