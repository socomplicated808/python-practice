from turtle import Turtle

class Projectile(Turtle):
    
    def __init__(self,start_x,start_y,color):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.shapesize(1,1,1)
        self.shape('triangle')
        self.color(color)
        self.speed(1)
        self.penup()
        self.setheading(90)
        self.goto(self.start_x,self.start_y)


    def move_forward(self):
        self.forward(5)
    

    def move_backward(self):
        self.setheading(270)
        self.forward(1)