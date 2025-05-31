
#inheritance

class Father:    # parent class
    Name = "MD HASAN"
    Age = 65
    Home = "BHOLA"

class Mother(Father):
    mName = "Jasmin Begum"
    mAge = 55
    mHome = "BHOLA"
class Child(Mother):  #child class which inherits multiple parent class
    name = "AZIZUL ISLAM"
    age = 22
    home = "BHOLA"



ch=Child()  # object of child
print(ch.Name)