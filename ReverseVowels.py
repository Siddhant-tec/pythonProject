from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimter(self):
        pass


class Square(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def perimter(self):
        print(self.l * self.b)


sq = Square(12, 15)
sq.perimter()
