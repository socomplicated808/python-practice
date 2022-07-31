import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pd.read_csv('50_states.csv')
states = states_data['state'].tolist()
#print(states_data[states_data['state'] == 'Hawaii']['x'].item())

game_on = True

myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.hideturtle()

checked = []
correct_guesses = 0

while game_on:
    user_guess = screen.textinput(f"States guess: {len(set(checked))}/50","Enter a state's name:").title()

    if user_guess == 'Exit':
        practice_states = []
        for state in states:
            if state not in checked:
                practice_states.append(state)
        data = pd.DataFrame(practice_states)
        data.to_csv('states_to_learn.csv')
        game_on = False

    if user_guess in states:
        x_pos = states_data[states_data['state'] == user_guess]['x'].item()
        y_pos = states_data[states_data['state'] == user_guess]['y'].item()
        myTurtle.goto(x_pos,y_pos)
        myTurtle.write(user_guess)
        checked.append(user_guess)
        correct_guesses += 1 
        
    if correct_guesses == 50:
        myTurtle.goto(0,0)
        myTurtle.clear()
        myTurtle.write("You Win!")
        game_on = False

#states_to_learn.csv