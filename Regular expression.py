

# Regular expression

# to use regular expression we should import re module

import re

print("Using [] metacharacter:")
tex ="I am Azizul islam Efath"  # declaring a text line
pattern="[a-z]"  # declaring a pattern to show all the lower character in the range of a to z
a= re.findall(pattern,tex)   # calling the findall method using re module
print(a)

print("\nUsing special sequence metacharacter:")



txt1 = "That will be 59 dollars"

#Find all digit characters:
x = re.findall("\d",txt1)
print(x)



# using start with pattern  ^
print("\nUsing ^ metacharacter:")
txt2 = "I am Azizul islam Efath"
patern="^I"  # the pattern indicates if the line start with the inserted value
b= re.findall(patern,txt2)

if b:
    print("The line starts with I")
else:
    print("The line does not start with I")
