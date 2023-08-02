# Task 2: After implementation, create an instance of each new class and for both, print out the result of the calc_perimeter method.

import abc

class Shape(object):
 __metaclass__ = abc.ABCMeta
 
@abc.abstractmethod

def calc_perimeter(self, input):
  
# Method documentation
 return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented:", perim)
        return perim
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_perimeter(self):
        perim = 2 * (self.length + self.width)
        print("Also consider me implemented:", perim)
        return perim

class Square(Rectangle):
   def __innit__(self, length):
      self.length = length
   
triangle_instance = Triangle(1, 2, 3)
triangle_instance.calc_perimeter()

rectangle_instance = Rectangle(4, 5)
rectangle_instance.calc_perimeter()

## unsure if need to do a square instance because in the UML diagram there is no calc_perimeter?