

x= 30  # global variable
b= 50

def Info():
    global x
    x=100  # local Variable
    print(x)
    print(b)

Info()
