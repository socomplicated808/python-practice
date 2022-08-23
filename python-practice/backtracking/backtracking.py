from turtle import Turtle,Screen
import time

ROWS = 3
COLUMNS = 5
SIZE = 100
HEIGHT = SIZE*ROWS
WIDTH = SIZE*COLUMNS

class Square(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.pendown()
        self.drawSquare()
        self.penup()

    def drawSquare(self):
        self.pencolor('black')
        self.pendown()
        for i in range(2):
            self.forward(SIZE)
            self.right(90)
            self.forward(SIZE)
            self.right(90)
        self.penup()

    def drawFillSquare(self,color):
        self.fillcolor(color)
        self.begin_fill()
        self.drawSquare()
        self.end_fill()
        self.fillcolor('white')


def backtracking(row,column):
    #out of bounds
    if row >= len(grid) or column >= len(grid[0]):
        return

    square = grid[row][column]
    
    #reaches the bottom right square
    if row == len(grid) - 1 and column == len(grid[0]) - 1:
        square.drawFillSquare('green')
        square.drawFillSquare('white')
        return

    square.drawFillSquare('yellow')
    backtracking(row,column+1)
    backtracking(row+1,column)
    square.drawFillSquare('white')
    square.drawSquare()




#screen settings
screen = Screen()
screen.setup(height=SIZE*ROWS+SIZE,width=SIZE*COLUMNS+SIZE)
screen.tracer(0)


grid = [[] for x in range(ROWS)]

#drawing the squares
for row in range(ROWS):
    for column in range(COLUMNS):
        xPos = column * SIZE - WIDTH/2
        yPos = (-row * SIZE) + HEIGHT/2  
        square = Square(xPos,yPos)
        grid[row].append(Square(xPos,yPos)) 


screen.update()
screen.tracer(1)

#start babcktracking visualization
backtracking(0,0)


screen.mainloop()