#single inheritance example

class Animal:
    def __init__(self,height,weight,color) -> None:
        self.height = height
        self.weight = weight
        self.color = color

    def info(self):
        print(f'height {self.height} weight {self.weight} and of color {self.color}')


    def sleep(self):
        print('sleeping')


    def walk(self):
        print('Starts Walking')

class Wolf(Animal):
    jaw_bite = 1200
    def __init__(self, height, weight, color, isAlpha):
        super().__init__(height, weight, color)
        self.isAlpha = isAlpha


    def hunt(self):
        print('Wolf Ready to hunt')

    

animal = Animal(500,2000,'brown')
wolf = Wolf(400,200,'white',True)
wolf.info()
wolf.sleep()
wolf.walk()
wolf.hunt()
animal.info()