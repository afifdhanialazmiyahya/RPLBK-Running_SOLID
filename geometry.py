import math

# Kelas untuk menghitung area persegi
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

# Kelas untuk menghitung area lingkaran
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Kelas untuk menampilkan hasil
class AreaPrinter:
    def print_area(self, shape):
        print(f"The area is: {shape.calculate_area()}")

# Penggunaan kelas
square = Square(4)
circle = Circle(5)

printer = AreaPrinter()
printer.print_area(square)  # Output: The area is: 16
printer.print_area(circle)  # Output: The area is: 78.53981633974483
