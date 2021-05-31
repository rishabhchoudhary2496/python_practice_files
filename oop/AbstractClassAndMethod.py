from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,breadth) -> None:
        super().__init__()
        self.length = length
        self.breadth = breadth

    def printArea(self):
        return self.length * self.breadth

r = Rectangle(100,200)
print(r)
print(r.printArea())

#cant object make of abstract class