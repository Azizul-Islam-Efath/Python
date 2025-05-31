
#inheritance

class Parent:
    a="i am the Parent class"

class Father(Parent):    # parent class
    b="I am the Father class which inherits from Parent"

class Mother(Parent):
    c="I am the Mother class which inherits from Parent"

class Child1(Father):  #child class which inherits multiple parent class
    d="I am the Child class which inherits from Father"

class Child2(Mother):
    e="i am the Child class which inherits from Mother"


print("Printing the hierarchy through the child class:\n")
f=Child1
g=Child2

print(f.a)
print(f.b)
print(f.d)

print("\n\n")
print(g.a)
print(g.c)
print(g.e)