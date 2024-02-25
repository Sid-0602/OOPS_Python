class Item:
    # class attributes:
    pay_rate= 0.8
    all = []

    #special method: __init__ is a constructor and it is called as soon as a object(instance) is created.
    # quantity=0 here defines that default (if parameter is not passed), the value should be 0. 
    def __init__(self,name:str ,price: float ,quantity=0):

        #assert is used to validate the arguments:
        assert price>=0, f"Price {price} is not greater than zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater than zero!"

        self.name = name #dynamic attributes assigned.
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    #the functions inside a class are called as methods.
    def calculate_total_price(self):
        total = self.price * self.quantity
        return total

    def applyDiscount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone",134.67,5) #instance of a class.
print(f"The total bill for {item1.name} = ", item1.calculate_total_price()) #the method when called always passes instance when this method is called.
item1.applyDiscount()
print(f"Price per item after discount = " , item1.price)

item2 = Item("Laptop",1233.90,3)
print(f"The total bill for {item2.name} = ",item2.calculate_total_price())

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)