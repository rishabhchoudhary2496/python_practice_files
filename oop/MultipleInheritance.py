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



class Mammal:
    def __init__(self):
        pass

    def give_birth(self):
        print('Give Birth')

    def walk(self):
        print('mammal walks')


class Wolf(Animal,Mammal):
    jaw_bite = 1200
    def __init__(self, height, weight, color, isAlpha):
        super().__init__(height, weight, color)
        self.isAlpha = isAlpha


    def hunt(self):
        print('Wolf Ready to hunt')


mammal = Mammal()
mammal.give_birth()
wolf = Wolf(100,300,'red',True)
wolf.walk()