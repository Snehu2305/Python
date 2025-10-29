class Calculator():
    
    

    def add(self, a  = None, b = None, d = None):
        
        if a is not None and b is not None and d is not None:
            s = a+ b+d
            print("Addition of three numbers: ", s)
        
        elif a is not None and b is not None:
             print("Addition of two numbers: ", a+b)
        elif a is not None:
            print("Printing the given parameter: ", a)
        else:
            print("No argument is passed")
    

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
d = int(input("Enter a number: "))


c = Calculator()
c.add()
c.add(a)
c.add(a, b)
c.add(a, b, d)