import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return self.radius * self.radius * math.pi