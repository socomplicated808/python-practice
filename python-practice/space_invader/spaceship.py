from turtle import Turtle

LEFT_WALL = -230
RIGHT_WALL = 230

class Spaceship(Turtle):

    def __init__(self,start_x,start_y,direction="right"):
        super().__init__()
        self.shape('turtle')
        self.speed(1)
        self.penup()
        self.color('white')
        self.setheading(90)
        self.start_x = start_x
        self.start_y = start_y
        self.direction = direction
        self.go_to_starting_position()

    def go_to_starting_position(self):
        self.goto(self.start_x,self.start_y)


    def player_move_left(self):
        if self.xcor() >= LEFT_WALL:
            self.left(90)
            self.forward(10)
            self.right(90)


    def player_move_right(self):
        if self.xcor() < RIGHT_WALL:
            self.right(90)
            self.forward(10)
            self.left(90)
    

    def enemy_move_left(self):
        if self.xcor() >= LEFT_WALL:
            self.left(90)
            self.forward(1)
            self.right(90)


    def enemy_move_right(self):
        if self.xcor() < RIGHT_WALL:
            self.right(90)
            self.forward(1)
            self.left(90)
    

    def enemy_move_down(self):
            self.right(180)
            self.forward(1)
            self.left(180)


    def update_position(self):
        if self.xcor() >= RIGHT_WALL:
            self.direction = "left"
        elif self.xcor() <= LEFT_WALL:
            self.direction = "right"
        if self.direction == "right":
            self.enemy_move_right()
        elif self.direction == "left":
            self.enemy_move_left()