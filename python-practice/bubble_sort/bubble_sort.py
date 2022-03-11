from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(height=500,width=1000)
screen.bgcolor('black')
screen.tracer(0)

start_y = -250

class Line(Turtle):

    def __init__(self,x_pos,height):
        super().__init__()
        self.x_pos = x_pos
        self.height = height
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(self.x_pos,start_y)
        self.setheading(90)
        self.pendown()
        self.forward(self.height)
        self.penup()


    def redraw_line(self):
        self.penup()
        self.goto(self.x_pos,start_y)
        self.pendown()
        self.forward(self.height)
        self.penup()


lines = []
numbers = [x for x in range(1,75)]
random.shuffle(numbers)

#generate the lines
for i in range(len(numbers)):
    #start drawing lines from -200 and separate them by 3 pixels
    #just for fun making the lines bigger by multiplying them by 4
    line = Line(-200 + i * 3, numbers[i] * 4)
    lines.append(line)


is_sorted = False
right = len(lines)


while not is_sorted:
    is_sorted = True

    #makes lines red and cyan
    for i in range(right - 1):
        line_one = lines[i]
        line_two = lines[i+1]
        line_one.clear()
        line_two.clear()
        screen.update()
        line_one.color('red')
        line_two.color('cyan')
        line_one.redraw_line()
        line_two.redraw_line()
        screen.update()

        #swaps position of red and blue and redraws the line as white
        if line_one.height > line_two.height:
            is_sorted = False
            line_one.height, line_two.height = line_two.height, line_one.height
            line_one.clear()
            line_two.clear()
            line_one.redraw_line()
            line_two.redraw_line()
            line_one.color('white')
            line_two.color('white')
            line_one.redraw_line()
            line_two.redraw_line()
        else:
            line_one.clear()
            line_two.clear()
            line_one.color('white')
            line_two.color('white')
            line_one.redraw_line()
            line_two.redraw_line()
    right -= 1

for i in range(len(lines)):
    lines[i].clear()
    lines[i].color('green')
    lines[i].redraw_line()
    screen.update()

screen.mainloop()