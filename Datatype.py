# string type data
from pickletools import pylist

name = "Name: Azizul Islam"
name_1 = " Efath"
print(name + name_1)
print(type(name))
print("\n")

# integer type data

Age = 22
print("AGE : ", Age)
print(type(Age))
print("\n")

# Floating type data

Cgpa = 3.69
print("CGPA : ", Cgpa)
print(type(Cgpa))
print("\n")

# Complex type data

Com = 124j
print("COMPLEX : ", Com)
print(type(Com))
print("\n")

# String formatting    printf(f"       {Operation/variable}   ")
user_name = "Sadia Jaman"
num1 = 20
num2 = 10
print(f"My name is:  {user_name}", )
print(f"Age : {num1 + num2}", )

                            # Binary type data
#Byte

arr=[1,2,5,4,7,8,9,6,3,20,50]
b=bytes(arr)
print(type(b))
print("\n")


#Bytearray

arr1=[1,2,5,4,7,8,9,6,3,20,50]
c=bytearray(arr1)
c[0]=100
print(c[0])
print(type(c))
print("\n")


#None type

x= None
print(x)
print(type(x))
print("\n")


                        #Sequence type data type

#List - kind of array with brachie []  ....mutable

Li = ["Efath","Sadia","Maria","Sumaiyea","Mishka"]
print(f"List type data     :{Li}")
Li[1]="Mishka"
print(f"After changing List:{Li}")

print(type(Li))
print("\n")


#tuple type data  - kind of array with brachie ()....immutable

tup = ("Azizul","Islam","Efath")
print(f"Tuple type data:{tup}")
print(type(tup))
print("\n")


# Range type data

ran = range(10)
for i in ran:            #for loop
    print(i)










































