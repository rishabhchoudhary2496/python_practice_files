#operator overloading and dunder methods
class Animal:
    def __init__(self,height,weight,color) -> None:
        self.height = height
        self.weight = weight
        self.color = color

    def info(self):
        return f'height {self.height} weight {self.weight} and of color {self.color}'


    def sleep(self):
        print('sleeping')


    def walk(self):
        print('Starts Walking')

    def __add__(self,other): #operator overloading + by using __add__ python calls it auto for +
        return self.weight + other.weight

    def __truediv__(self,other): 
        return self.weight / other.weight

    def __sub__(self,other):
        return abs(self.weight - other.weight)

    # def __repr__(self) -> str: #returns string repersentaion of object
    #     return f"Animal({self.weight}, {self.height}, '{self.color}')"

    def __str__(self):
        return self.info()

panda = Animal(30,70,'black&white')
bear = Animal(30,230,'black')
print(bear)

print(panda+bear)
print(panda/bear)
print(bear-panda)
# + class __add__ methods 

# if both __str__ and __repr__ then __str__ will be called
#repr represents object in string format
#str represent humable readable string