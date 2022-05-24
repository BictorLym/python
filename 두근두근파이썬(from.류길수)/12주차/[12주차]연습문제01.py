#PI = 3.141592
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.141592

    def calcPerimeter(self):
        peri = 2 * self.PI * self.radius
        return peri

    def calcArea(self):
        return self.PI * (self.radius ** 2)

mycircle = Circle(100)

length = mycircle.calcPerimeter()
print(f'반지름: {mycircle.radius}  ')
print(f'원의면적: {mycircle.calcArea()}  ')
print(f'원의둘레: {length}  ')
