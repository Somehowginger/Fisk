import math

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
    
    def __mull__(self, scalar):
        return (self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Division by zero is not allowed.")
        return (self.x / scalar, self.y / scalar)
    
    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        length = self.getLength()
        if length == 0:
            raise ValueError("Cannot normalize a vector with length 0.")
        return (self.x / length, self.y / length)
    
    def distance(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        return math.sqrt(diff_x**2 + diff_y**2)

    def get_x(self):
        return self.x
    
    def set_x(self,x):
        self.x = x
