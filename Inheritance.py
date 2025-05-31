
#inheritance

class Father:    # parent class
    Name = "MD HASAN"
    Age = 65
    Home = "BHOLA"

class Child(Father):  #child class which inherits
    name = "AZIZUL ISLAM"
    age = 22
    home = "BHOLA"

ch=Child()  # object of child
print(ch.Name)