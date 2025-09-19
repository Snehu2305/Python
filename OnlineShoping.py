from abc import ABC

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 


class Cart:
    def __init__(self):
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)
    
    def removeProduct(self, product):
        if product in self.products:
            self.products.remove(product)
    
    def calculateTotal(self):
        return sum(p.price for p in self.products)
    

class Discount(ABC):
    def apply(self, total):
        pass

class  PercentDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent
    
    def apply(self, total):
        return total - (total * self.percent / 100)
    
class FlatDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, total):
        return total - self.amount

class Payment(ABC):
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"paid{amount} using Credit card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"paid{amount} through UPI")


p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)

cart = Cart()
cart.addProduct(p1)
cart.addProduct(p2)

total = cart.calculateTotal()
print("Total: ", total)

discount = PercentDiscount(10)
total = discount.apply(total)
print("After Discount: ", total)

Payment = UPIPayment()
Payment.pay(total)


    
