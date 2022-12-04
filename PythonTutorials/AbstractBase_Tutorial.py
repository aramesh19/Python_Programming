from abc import ABC, abstractmethod
# when some classes inherit ABC then such classes force their child classes to use/implement some of the methods
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = 'Rectangle'
    side = 4

    def __init__(self):
        self.length = 10
        self.width = 4

    def printarea(self):
        return self.length * self.width

R1 = Rectangle()
print(R1.printarea())

tryobj = Shape() # Can't instantiate abstract class