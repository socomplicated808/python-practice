from tkinter import *
from tkinter import filedialog
from PIL import Image

def get_colors():
    file = filedialog.askopenfile()
    image_name = file.name
    image = Image.open(image_name)
    pixels = image.load()
    height,width = image.size
    hex_codes = {}
    
    
    #gets all hexcodes
    for y in range(width):
        for x in range(height):
            try:
                r,g,b = pixels[x,y]
            except ValueError:
                r,g,b,a = pixels[x,y]
            hex_code = "#" + "{:02x}{:02x}{:02x}".format(r,g,b)
            if hex_code in hex_codes:
                hex_codes[hex_code] += 1
            else:
                hex_codes[hex_code] = 1
    
    #gets the 10 most common hex codes
    sorted_hex = sorted(hex_codes.items(),key=lambda x:x[1],reverse=True)

    for widget in window.winfo_children():
        widget.destroy()
    
    for i in range(len(sorted_hex[:10])):
        color_label = Label(text=sorted_hex[i][0],bg=sorted_hex[i][0],height=10,width=10)
        color_label.grid(row=0,column=i)


window = Tk()

open_file_label = Label(text='Select File:')
open_file_label.grid(row=0,column=0,padx=10)
open_file_button = Button(text='Open',command=get_colors)
open_file_button.grid(row=0,column=1)

window.mainloop()