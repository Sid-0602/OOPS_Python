class Animal: 
    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("This animal is sleeping")

    def move(self):
        print("This animal moves!")


#rabbit class is child class of Animal class.
class Rabbit(Animal):
    pass
class Fish(Animal):

    #this method overrides the parent method.
    def move(self):
        print("This fish is sleeping")
    
class Hawk(Animal):
    def move(self):
        print("This hawk is flying.")

class AmericanHawk(Hawk):
    def move(self):
        print("This is American hawk and it flies more.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
americanHawk = AmericanHawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.move()
fish.move()
hawk.move()
americanHawk.move() #child of hawk which is child of Animal.
