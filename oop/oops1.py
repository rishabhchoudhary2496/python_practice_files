class Car:
    wheel = 4
    def __init__(self,color,model,year): 
        self.color = color
        self.model = model
        self.year = year
    
    def info(self):
        print(f'Color {self.color} Model {self.model} Year{self.year}')


    def move(self):
        pass #pass results in no operation use as a placeholer for no syntax error
 
    def applybreak (self):
        print('Applying Break')


my_car = Car('red','subaru',2012)
new_car = Car('blue','hyundai',2011)
print(my_car is new_car)
my_car.info()
print(Car.wheel)
