
class Method :

# instance method
    def instance(self):
        print('instance method')

# classmethod
    @classmethod     # classmethod function called
    def Classm(cls):
        print('class method')

# static method
    @staticmethod
    def Static():
        print('static method')


m1 = Method()  # created object of the class

m1.instance()  # instance method can only be called by object

m1.Classm()  # Classmethod can be called by both class and object ,it must have parameter

m1.Static()  # same as class method , u can use parameter or not,it's up to u

