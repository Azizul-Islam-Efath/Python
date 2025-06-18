
class Vehicle:
    def __init__(self,model,brand, year):
        self.model = model
        self.year = year
        self.brand = brand


class Plane(Vehicle): # Inheritance used
    pass

p=Plane("Boeing747","Emirates",1971)
print("Plane Info: \n")
print(f"This is     : {p.model}\nBelongs to  : {p.brand}\nSince       : {p.year}\n\n")


class Car(Vehicle):
    pass

c = Car("I8","BMW", 1999)
print("Car Info: \n")
print(f"This is     : {c.model}\nBelongs to  : {c.brand}\nSince       : {c.year}")
