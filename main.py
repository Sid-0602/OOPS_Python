class Item:
    #special method: __init__ is a constructor and it is called as soon as a object(instance) is created.
    def __init__(self,name,price,quantity=0):
        print(f"Instance created: {name}")
        self.name = name #dynamic attributes assigned.
        self.price = price
        self.quantity = quantity

    #the functions inside a class are called as methods.
    def calculate_total_price(self):
        total = self.price * self.quantity
        return total

item1 = Item("Phone",134.67,5) #instance of a class.
print(item1.calculate_total_price()) #the method when called always passes instance when this method is called.
print(item1.name)

item2 = Item("Laptop",1233.90,3) #instance of a class.
print(item2.calculate_total_price())