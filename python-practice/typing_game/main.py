import random
from tkinter import *
from tkinter import messagebox
from wordlist import words


score = 0
timer = 60

window = Tk()
window.title('Typing Game')


#-----------------Functions-------------------
def decrease_timer():
    global timer
    global score
    start_button.config(state='disabled')
    typing_bar.focus()
    timer = timer - 1
    timer_label.config(text=f"{timer} seconds remaining")
    countdown = window.after(1000,decrease_timer)
    if timer == 0:
        window.after_cancel(countdown)
        messagebox.showinfo(title="Words Typed",message=f"You typed {score} words in 60 seconds.")
        start_button.config(state='active')
        score = 0
        score_label.config(text=f"Score: {score}")
        timer = 60
        timer_label.config(text=f"{timer} seconds remaining")


def change_to_default():
    window.config(bg='SystemButtonFace')
    word_label.config(bg='SystemButtonFace')
    timer_label.config(bg='SystemButtonFace')
    score_label.config(bg='SystemButtonFace')


def change_to_green():
    window.config(bg='green')
    word_label.config(bg='green')
    timer_label.config(bg='green')
    score_label.config(bg='green')
    window.config(bg='green')
    window.after(100,change_to_default)


def change_to_red():
    window.config(bg='red')
    word_label.config(bg='red')
    timer_label.config(bg='red')
    score_label.config(bg='red')
    window.after(100,change_to_default)


def update_screen(event):
    global score
    label_word = word_label.cget('text')
    word = typing_bar.get("1.0",'end-1c').strip()
    typing_bar.delete("1.0","end")
    
    #changes the word to type to a new word
    word_label.config(text=random.choice(words))

    if word == label_word:
        window.after(5,change_to_green)
        score += 1
        score_label.config(text=f"Score: {score}")
    elif word != label_word:
        window.after(5,change_to_red)


#-----------------Labels-------------------
word_label = Label(text=random.choice(words),font=("Arial",75,'normal'))
word_label.grid(row=1,column=1)
timer_label = Label(text=f"{timer} seconds remaining",padx=20)
timer_label.grid(row=0,column=0)
score_label = Label(text=f"score: {score}",padx=20)
score_label.grid(row=0,column=2)


#-----------------Entries-------------------
typing_bar = Text(height=1,width=20,font=("Arial",16,'normal'))
typing_bar.grid(row=2,column=1,pady=20)



#-----------------Buttons-------------------
start_button = Button(text='START',command=decrease_timer)
start_button.grid(row=3,column=1)


typing_bar.bind("<Return>",update_screen)


window.mainloop()