# Print function
print("Hello World")
print("More strings")
print(3)
# Variables
a=1
print(a)
b=2
print(b)
c="Hello there"
print(c)
# you can reasign an existing variable to another value
b=1
print(b)
# you can't print unavailable variable
# print(e) will give an error
e=3
print(e)
# you can asign a variable to another variable
f=a
print(f)
# if you reasign a a different value, the value of f remains at the previous value.
a=4
print(a,f)
# the output is 4 and 1 respectively

# Swapping variables
v1="first string"
v2="second string"

# swap without repeting the strings interchangably.
# introduce temporary variables
t1=v1
t2=v2
v1=t2
v2=t1
print(v1,",",v2)

# Better way is to use one temporary variable
t=v1
v1=v2
v2=t
print(v1,",",v2)

# assining multiple values to multiple variables
a,b,c=3,"man","dog"
print(a)
print(b)
print(c)

# we can assign same value to multiple variables
name1=name2="Ochieng_Onyango"
print(name1)
print(name2)