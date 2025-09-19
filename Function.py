def Calculator(x, y, operation):
    if operation == "add":
       return x+y
    
    elif operation == "subtract":
       return x - y
    
    elif operation == "multiply":
       return x * y
    
    elif operation == "divide":
       return x / y
    
    elif operation == "power":
       return x ** y
    
    else:
       print("Not a valid operation. Please enter valid operation")



print(Calculator(12, 45, "add"))
print(Calculator(50, 25, "subtract"))
print(Calculator(18, 40, "multiply"))
print(Calculator(90, 45, "divide"))
print(Calculator(12, 3, "power"))
print(Calculator(180, 45, "modulo"))