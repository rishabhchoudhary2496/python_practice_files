#MultiLevel inheritance example

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



class Mammal(Animal):
    def __init__(self,height, weight, color):
        super().__init__(height, weight, color)

    def give_birth(self):
        print('Give Birth')

    def walk(self):
        print('mammal walks')


class Wolf(Mammal):
    jaw_bite = 1200
    def __init__(self, height, weight, color, isAlpha):
        super().__init__(height, weight, color)
        self.isAlpha = isAlpha

    def hunt(self):
        print('Wolf Ready to hunt')

    def walk(self):
        print('wolf walks with pride')


wolf = Wolf(100,300,'red',True)
wolf.walk()
wolf.give_birth()