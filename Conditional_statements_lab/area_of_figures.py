from math import pi

figure = str(input())

if figure == "square":
    a = float(input())
    area_of_the_square = a * a
    print(f"{area_of_the_square:.3f}")

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area_of_the_rectangle = a * b
    print(f"{area_of_the_rectangle:.3f}")

elif figure == "circle":
    a = float(input())
    area_of_the_circle = a * a
    area_of_the_circle2 = area_of_the_circle * pi
    print(f"{area_of_the_circle2:.3f}")

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area_of_the_triangle = a * h / 2
    print(f"{area_of_the_triangle:.3f}")
from math import pi

figure = str(input())

if figure == "square":
    a = float(input())
    area_of_the_square = a * a
    print(f"{area_of_the_square:.3f}")

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area_of_the_rectangle = a * b
    print(f"{area_of_the_rectangle:.3f}")

elif figure == "circle":
    a = float(input())
    area_of_the_circle = a * a
    area_of_the_circle2 = area_of_the_circle * pi
    print(f"{area_of_the_circle2:.3f}")

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area_of_the_triangle = a * h / 2
    print(f"{area_of_the_triangle:.3f}")
