class Car:
    def __init__(self,color,model,year): 
        self.color = color
        self.model = model
        self.year = year
    
    def info(self):
        print(f'Color {self.color} Model {self.model} Year{self.year}')


 

my_car = Car('red','subaru',2012)
my_car.info()
