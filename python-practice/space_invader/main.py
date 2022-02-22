from turtle import Turtle,Screen
from spaceship import Spaceship
from projectile import Projectile
import random


screen = Screen()
screen.setup(height=500,width=500)
screen.bgcolor('black')
screen.tracer(0)

game_on = True
player = Spaceship(0,-230)
projectiles = []
enemy_projectiles = []
enemies = []

for y in range(230,30,-40): #creates 5 rows of enemies
    for x in range(-150,190,40): #creates 5 turtles per row
        enemy = Spaceship(x,y,direction="right")
        enemies.append(enemy)

def game_over():
    global game_on
    for enemy in enemies:
        enemy.hideturtle()
    for projectile in enemy_projectiles:
        projectile.hideturtle()
    for projectile in projectiles:
        projectile.hideturtle()
    player.hideturtle()
    game_on = False
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.color('red')
    turtle.goto(0,0)
    turtle.write("GAME OVER",align='center',font=("Arial",24,"normal"))


def game_win():
    global game_on
    for enemy in enemies:
        enemy.hideturtle()
    for projectile in enemy_projectiles:
        projectile.hideturtle()
    for projectile in projectiles:
        projectile.hideturtle()
    player.hideturtle()
    game_on = False
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.color('green')
    turtle.goto(0,0)
    turtle.write("YOU WIN",align='center',font=("Arial",24,"normal"))


def make_missile():
    #only allows one missle to be fired at a time
    if len(projectiles) == 0:
        projectile = Projectile(player.xcor(),player.ycor(),'green')
        projectiles.append(projectile)


def make_enemy_missile(enemy):
    if len(enemy_projectiles) <= 4:
        fire_chance = [False for x in range(200)]
        fire_chance.append(True)
        fire_ok = random.choice(fire_chance)
        if fire_ok:
            projectile = Projectile(enemy.xcor(),enemy.ycor(),'red')
            enemy_projectiles.append(projectile)


screen.listen()
screen.onkeypress(player.player_move_left,'Left')
screen.onkeypress(player.player_move_right,'Right')
screen.onkeypress(make_missile,'space')

while game_on:
    #move the missiles forward. Deletes the projectile object when it moves offscreen
    for i in range(len(projectiles)):
        projectiles[i].move_forward()
        if projectiles[i].ycor() > 260:
            del projectiles[i]
            break

        for j in range(len(enemies)):
            if projectiles[i].xcor() >= enemies[j].xcor() - 10 and projectiles[i].xcor() <= enemies[j].xcor() + 10:
                if projectiles[i].ycor() >= enemies[j].ycor() - 10 and projectiles[i].ycor() <= enemies[j].ycor() + 10:
                    enemies[j].hideturtle()
                    projectiles[i].hideturtle()
                    del projectiles[i]
                    del enemies[j]
                    break
        
        if len(enemies) == 0:
            game_win()

    for i in range(len(enemy_projectiles)):
        enemy_projectiles[i].move_backward()
        
        #deletes the projectile once its off screen
        if enemy_projectiles[i].ycor() < -260:
            del enemy_projectiles[i]
            break
        
        #game over if the projectil hits the player
        if enemy_projectiles[i].ycor() - 10 == player.ycor() + 10\
            and enemy_projectiles[i].xcor() > player.xcor() - 10 \
            and enemy_projectiles[i].xcor() < player.xcor() + 10:
            game_over()

    for i in range(len(enemies)):

        #changes directions when enemies hit the edge and move them downward
        if enemies[i].xcor() >= 230:
            for j in range(len(enemies)):
                enemies[j].direction = "left" 
                enemies[j].enemy_move_down()
        elif enemies[i].xcor() <= -230:
            for j in range(len(enemies)):
                enemies[j].direction = "right"
                enemies[j].enemy_move_down() 
        if enemies[i].ycor() <= -230:
            game_over()
            break
        enemies[i].update_position()
        make_enemy_missile(enemies[i])
        


    screen.update()



screen.mainloop()
