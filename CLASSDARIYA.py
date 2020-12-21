class Car:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
        self.fuel=100
        self.run=0
        self.color='orange'
        self.no2=False

    def move(self,distanse):
        if distanse>0:
            result=20/100
            result=distanse*result
            self.fuel-=result
            self.run+=distanse
car1=Car('tesla','xs',9000)
print(car1.run)
car1.move(240)
print(car1.run)
print(car1.fuel)
