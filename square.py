class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class CircleInSquare(Square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def calculate_radius(self):
        return self.side_length / 2

    def calculate_circle_area(self):
        radius = self.calculate_radius()
        return 3.14 * radius ** 2



if __name__ == "__main__":
    square = Square(4)
    print(f"Square Area: {square.calculate_area()}")

    circle_in_square = CircleInSquare(4)
    print(f"Circle Radius: {circle_in_square.calculate_radius()}")
    print(f"Circle Area inscribed in the Square: {circle_in_square.calculate_circle_area()}")
