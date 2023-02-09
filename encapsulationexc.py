class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * side
        self._area = side * side
        self._diagonal = (2 ** 0.5) * side

    def get_side(self):
        return self._side

    def set_side(self, new_length):
        self._side = new_length
        self._perimeter = 4 * new_length
        self._area = new_length * new_length
        self._diagonal = (2 ** 0.5) * new_length

    def get_perimeter(self):
        return self._perimeter

    def set_perimeter(self, new_perimeter):
        self._side = new_perimeter / 4
        self._perimeter = new_perimeter
        self._area = (new_perimeter / 4) ** 2
        self._diagonal = (2 * (new_perimeter / 4)) ** 0.5

    def get_area(self):
        return self._area

    def set_area(self, new_area):
        self._side = new_area**0.5
        self._perimeter = 4 * (new_area ** 0.5)
        self._area = new_area
        self._diagonal = (2 * (new_area ** 0.5)) ** 0.5

    def get_diagonal(self):
        return self._diagonal

    def set_diagonal(self, new_diagonal):
        self._side = new_diagonal / (2 ** 0.5)
        self._perimeter = 4 * (new_diagonal / (2 ** 0.5))
        self._area = ((new_diagonal / (2 ** 0.5)) ** 2)
        self._diagonal = new_diagonal


# obj = Square(4)
# print(obj._diagonal) #LMAOPYTHON
obj = Square(5)
print(obj.get_area())

obj.set_perimeter(345)
print(obj.get_perimeter())
print(obj.get_side())