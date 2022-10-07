class budget:

    def __init__(self, Entertainment, Shoppingprice):
        self.Entertainment=Entertainment
        self.Shoppingprice=Shoppingprice

    def buyclothes(self):
        print("I want to buy clothes")    

object1 = budget("See a movie", 20000)

print(object1.buyclothes())

class Animal:
    animal_type = "mammal" 
    counter = 0 

    def __init__(self, name, number_of_legs):
        self.name=name
        self.number_of_legs=number_of_legs
        Animal.counter += 1

    def can_run(self):
        print(f"A {self.name} runs with {self.number_of_legs} Legs")

animal_one=Animal("Jaguar", 4) 
animal_two=Animal("Panther", 4)  

animal_one.can_run()
animal_two.can_run()

class Animals:

    def can_breathe(self):
        return "Animals can breathe"

class mammals(Animals):
    pass

mammal_one=mammals().can_breathe()
print(mammal_one)