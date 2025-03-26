from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def area(self):
      print("triangle has 3 sides")

class Pentagon(Polygon):
   def area(self):
      print("pentagon has 5 sides")

t = Triangle()
t.area()

p = Pentagon()
p.area()



