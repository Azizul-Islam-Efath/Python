class Parent:
    def __init__(self, name, age):
        self.__name = name   # made private using double underscore
        self.__age = age
        print(f"My name is {self.__name} and my age is {self.__age}")

p = Parent("I8", 1999)


