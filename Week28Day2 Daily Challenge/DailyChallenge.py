import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        self.radius = radius if radius else diameter / 2
        
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius:.2f}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=3)


print(c1)  # radius 5.00
print(f"Area of c1: {c1.area:.2f}")  # 78.54


c4 = c1 + c3
print(c4)  # adius 8.00

# Comparison of circles
print(c1 > c3)  True
print(c1 == c2) True
print(c1 == c3) False
