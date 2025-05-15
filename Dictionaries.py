

# creating dictionary  - it is ordered, changeable, does not allow duplicate
print("-------------Python dictionary---------------\n")

myinfo = {
    "Efath":{
        "Name": "Azizul islam",
        "location": "Dhaka",
        "University":"Daffodil International university",
        "ID":"241-35-364"
    },
    "Maria":{
        "Name": "Zannatul Farzana",
        "location": "Dhaka",
        "University":"Daffodil International university",
        "ID":"241-35-106"
    },

    "Mishka":{
        "Name": "Sadia Jaman Misho",
        "location": "Dhaka",
        "University":"Daffodil International university",
        "ID":"241-35-399"
    },
    "Sumaiyea":{
        "Name": "Sumaiyea binte faruque",
        "location": "Dhaka",
        "University":"Daffodil International university",
        "ID":"241-35-007"
    }
}

# for loop
print("\nEfath's info: \n")
for i in myinfo["Efath"]:
    print(myinfo["Efath"][i])

print("\nMishkas's info: \n")
for i in myinfo["Mishka"]:
    print(myinfo["Mishka"][i])

print("\nMaria's info: \n")
for i in myinfo["Maria"]:
    print(myinfo["Maria"][i])

print("\nSumaiyea's info: \n")
for i in myinfo["Sumaiyea"]:
    print(myinfo["Sumaiyea"][i])


''' basic 
print((myinfo["Efath"]["Name"]))
print((myinfo["Efath"]["location"]))
print((myinfo["Efath"]["University"]))
print((myinfo["Efath"]["ID"]))
'''

#get method

x=myinfo.get("Efath")
print("\nUsing get method : ",x)

# key method

y=myinfo.keys()
print("\nKeys in the dictionary : ",y)

#values method
z=myinfo.values()
print("\nValues in the dictionary : ",z)

#update dictionary

myinfo["Efath"]["Name"]= "Azizul islam (Efath)"

print("\nAfter updating Efath's info : \n")

for i in myinfo["Efath"]:
    print(myinfo["Efath"][i])

print("\n\n")

#update method

A= myinfo.update({"Efath":"Efath is a SOFTWARE ENGINEER"})
print("\nAfter using update method Efath's info : ",myinfo["Efath"])















