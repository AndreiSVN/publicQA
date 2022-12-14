#                               полиморфизм и наследование в расчетах площади фигур
# import math
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_area_square(self):
#         return self.a ** 2
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area_circle(self):
#         return round(((self.radius**2) * math.pi), 2)
#
# ========================================================================
# from Test import Rectangle, Square, Circle
# r1 = Rectangle(3, 4)
# r2 = Rectangle(12, 5)
# print(f'площадь прямоуголника r1 равна {r1.get_area()}')
# print(f'площадь прямоуголника r2 равна {r2.get_area()}')
#
# s1 = Square(5)
# s2 = Square(10)
# print(f'площадь квадрата s1 равна {s1.get_area_square()}')
# print(f'площадь квадрата s2 равна {s2.get_area_square()}')
#
# c1 = Circle(6)
# c2 = Circle(12)
# print(f'площадь круга c1 равна {c1.get_area_circle()}')
# print(f'площадь круга c1 равна {c2.get_area_circle()}')
#
# figures = [r1, r2, s1, s2, c1, c2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     elif isinstance(figure, Circle):
#         print(figure.get_area_circle())
#     else:
#         print(figure.get_area())
