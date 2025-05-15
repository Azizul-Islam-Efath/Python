
#Creating set

newSet= {1,2,4,3,4,True,False,"string",2}
print("Type of the data : ",type(newSet))
print("THE SET IS : ",newSet)
print("The length of the set : ",len(newSet))

# Accessing set item
print("Access set data: \n")

for i in newSet:
    print(i)

#finding value if available or not
print("Is the value 5 available ? :",5 in newSet)

#Add set item

Set = {1,2,3,4,5,6,7,8,9,10}
print("----------Set-------------\n Type of the data : ",type(Set))

print("\nTHE SET IS : ",Set)
Set.add(11)       # variable.add(data type)
print("\nAfter adding item, the set is :",Set)

# Set update method

Set1 = [10,20,30,40]

print("\nNew set : ",Set1)
Set.update(Set1)

print("\nUpdated set is :",Set)

# Remove set item  (Duplicate hobe na,  structure different, change krta parbo na)

Set3 ={4,3,2,5,6,7}

print("\ninitially Set 3 is : ",Set3)
Set3.remove(7)           # variable.remove(data)
print("\nAfter removing item 7 the set is : ",Set3)

Set3.discard(8)  # Set a jodi data ta available na o thake tao error diba na execute krba
print("\nAfter Discard 8 the set is : ",Set3)

Set3.pop()
print("\nAfter popping item the set is : ",Set3)

#Set3.clear()
#print("\nAfter clearing the set is : ",Set3)

# Loop in set

print("\n-------------For Loop in Set---------------\n")

for i in Set3:
    print(i)

# join sets

s1={"a","b","c"}
print("\nS1 = ",s1)
s2={1,2,3,4}
print("\nS2 = ",s2)
s3=s1.union(s2)    # variable1.union(variable2)
print("\nAfter Union : ",s3)



















