class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def apply_tax(self,percent):
        self.price=self.price+(percent/100*round(self.price,2))
       

c=Car('Volks Wagon',12000)
obj=Car('Verna Monstare',340000)
obj.apply_tax(28)
print('Total price of verna including 28% tax::',obj.price)
c.apply_tax(18)
print(c.price)
print()

class Player:
    def __init__(self,name,score=0):
        self.name=name
        self.score=score

    def incres_score(self,points):
        self.score+=points

    def show_score(self):
        print(self.score)


obj=Player('Rahul',200)
obj2=Player('Rajeev',100)
obj2.incres_score(4.5)
obj2.show_score()
obj.incres_score(2.4)
obj.show_score()
print()
class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def compare(cls,other_laptop):
        






        
    


        



    
