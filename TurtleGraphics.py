#TurtleGraphics.py
#Name: Maverick Piper
#Date: 9/22/2024
#Assignment:Lab 3

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(bob, corner):
    #draw big sqare
    drawSquare(bob, 100)
   
    if corner == 1:
        bob.begin_fill()
        drawSquare(bob, 50)   
        bob.end_fill()
    elif corner == 2:
        bob.forward(50)
        bob.begin_fill()
        drawSquare(bob, 50)   
        bob.end_fill()
    elif corner == 3:
        bob.forward(50)
        bob.begin_fill()
        drawSquare(bob, 50)   
        bob.end_fill()
    elif corner == 4:
        bob.forward(50)
        bob.begin_fill()
        drawSquare(bob, 50)   
        bob.end_fill()

bob = turtle.Turtle()

def draw_square(size):
    for _ in range(4):
        bob.forward(size)
        bob.right(90)


def squaresInSquares(number_of_squares, initial_size, gap):
    for i in range(number_of_squares):
        draw_square(initial_size + i * gap)
        bob.penup()
        bob.goto(-gap * (i + 1) / 2, -gap * (i + 1) / 2)
        bob.pendown()

number_of_squares = 5
initial_size = 20
gap = 20

squaresInSquares(number_of_squares, initial_size, gap)
    
    #drawPolygon(bob, 5) #draws a pentagon
    #drawPolygon(bob, 8) #draws an octogon
    #drawPolygon(bob, 3)

    #fillCorner(bob, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(bob, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
