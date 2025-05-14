# tuple syntax   variable = ()

tup = (1, 2, 3, 4, True, False)

print(f"\n Type of the data : {type(tup)}")

# accessing data by minus indexing

print(f"\n Negative indexing \n Index [-1]:{tup[-1]}")

# Range of index  Syntex-   tup[starting index, ending index+1]

print(f"\n Accessing tuple with range: {tup[0:6]}")

# updating tuple

x = list(tup)

print("\n Printing List ", x)

x.append(6)

tup = tuple(x)

print("\n Updated Tuple: ", tup)

# Unpack tuple

print("\nUnpacking tuple: \n")
new = ("Ab", "Bc", "Cd", "De", 4, 3, 5)

(w, x, y, *z, a) = new  # '*' indicates this variable holds the last elements which are not defined

print("\n", z)

# Loop in tuple
print("\nTuple loop: \n")

for i in new:
    print(i)

print("\nfor using range:\n")

for i in range(len(new)):
    print(new[i])

print("\ntuple using while loop:\n")

l = 0
while l < len(new):
    print(new[l])
    l = l + 1

# join tupple
print("\njoin two tuples:\n")

tup1 = (1, 2, 3, 4, 5, 6)
print("Tuple one : ", tup1 * 2)  # multiplying tuple
tup2 = (7,7,7, 8, 9, 10, 11, 12)
print("\nTuple two : ", tup2)

tup = tup1 + tup2
print("\nJoint tuple :", tup)

cou = tup.count(7)
print("counting 7 how many time it used : ",cou)

print("value 3 is at index no :",tup.index(3))




