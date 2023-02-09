class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f'Middle point is on: {self.x} and {self.y}. Its color is ' + self.color)
        return

    def distance(self, other_shape):
        result = ((self.x + other_shape.y)**2 + (self.y + other_shape.x)**2)**0.5
        return print(result)


a = Shape(6, 2, 'blue')
b = Shape(4, 7, 'red')
a.describe()
b.describe()
a.distance(b)
b.distance(a)