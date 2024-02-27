'''Assignment
Start by completing the core requirements. Then, when that part is complete, if you have time, see if you can complete some of the stretch challenges as well.

Core Requirements
Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

An example run of the program might look something like the following:


What is the length of a side of the square? 5
The area of the square is: 25.0
What is the length of rectangle? 6
What is the width of the rectangle? 7
The area of the rectangle is: 42.0
What is the radius of the circle? 5
The area of the circle is: 78.5  '''
import math
def print_areas():
    #Area of a square 
    side =float(input("What is the length of a side of the square? "))
    area = side ** 2
    print(f"The area of the square is: {area}")
    
    #Area of a rectangle
    lenght = float (input("What is the length of a rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = lenght * width
    print(f"The area of the recatngle is: {area}")
    
    #Area of a circle
    radius = float(input("What is the radius of a circle? "))
    area = math.pi * (radius ** 2)
    print(f"The area of a circle is: {area:.1f}")
print_areas()