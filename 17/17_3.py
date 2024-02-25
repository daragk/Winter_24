class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def set_colour(self, colour): #установить цвет
        self.colour = colour
    def set_square(self, square): #установить площадь
        self.square = square
    def get_colour(self): #запросить цвет объекта и напечатать его
        print(self.colour)
    def get_square(self): #запросить площадь объекта
        return self.square
circle = Shape('red', 555)
triangle = Shape('blue', 13)

print(triangle.get_square())
triangle.get_colour()