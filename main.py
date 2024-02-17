class Item:
    #special method: __init__ is a constructor and it is called as soon as a object(instance) is created.
    # quantity=0 here defines that default (if parameter is not passed), the value should be 0. 
    def __init__(self,name:str ,price: float ,quantity=0):

        #assert is used to validate the arguments:
        assert price>=0, f"Price {price} is not greater than zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater than zero!"

        self.name = name #dynamic attributes assigned.
        self.price = price
        self.quantity = quantity

    #the functions inside a class are called as methods.
    def calculate_total_price(self):
        total = self.price * self.quantity
        return total

item1 = Item("Phone",134.67,5) #instance of a class.
print(f"The total bill for {item1.name} = ", item1.calculate_total_price()) #the method when called always passes instance when this method is called.

item2 = Item("Laptop",1233.90,3)
print(f"The total bill for {item2.name} = ",item2.calculate_total_price())