from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import random

root = Tk()#main window
root.title("Alexa - Tell Me a Joke")#name of app
root.minsize(1500, 800)#size for window

bgimg = 'C:/Users/eriel/Desktop/Code Lab II SA1/02- Alexa tell me a Joke/jokebg.png'#linking the image
orgimg = Image.open(bgimg).resize((1500, 800))#resizing the background image
jokebg = ImageTk.PhotoImage(orgimg)#making the image as the background image

jokeimg = Label(root, image=jokebg)#placing the backgrond image in the main window
jokeimg.place(x=0, y=0, relwidth=1, relheight=1) #fitting the image to the whole window

Big_text = Font(family="Century Gothic", size=25, weight="bold")#font for big text
Btn_text = Font(family="Times New Roman Greek", size=15, weight="bold")#font for buttons
jokes = 'C:/Users/eriel/Desktop/Code Lab II SA1/02- Alexa tell me a Joke/randomJokes.txt'#linking txt file to python file

with open(jokes, 'r') as file:#opening the txt file
    jokes = file.readlines()#reading all the lines in the txt file
    jokes = [joke.strip() for joke in jokes if joke.strip()]#removing all the empyt lines in the txt file

def tell_joke():#function to show a random joke
    joke = random.choice(jokes)#using random to show a random joke
    setup, punchline = joke.split('?')#using split function to seperate the punchling and the joke
    setup_label.config(text=f"{setup}?")#displaying the joke as a text
    punchline_label.config(text="") #clearning the punline text using config
    punchline_button.config(state=NORMAL, command=lambda: show_punchline(punchline))#to show punchline when the button is clicked
    
def show_punchline(punchline):#function to show the punchline
    punchline_label.config(text=f"{punchline}")#using config to show punchlin as text
    punchline_button.config(state=DISABLED)#disabling the button when there is no jokes

def quit_app():#function to quit the app when button is pressed
    root.quit()#end the app

setup_label = Label(root, text="Press the button for a joke!", wraplength=500, font=Big_text, bg="white", fg="black")#text for introduction
setup_label.place(x=550, y=120)

punchline_label = Label(root, text="", wraplength=500,font=Big_text, bg="white", fg="black", )#text for punchline is blank
punchline_label.place(x=590, y=350)

punchline_button = Button(root, text="Show Punchline", padx=50, pady=20, bg="#e42d25", fg="black", 
font=Btn_text, border=10,state=DISABLED)#button for punchline
punchline_button.place(x=250, y=580)

tell_joke_button = Button(root, text="Tell me a joke!", padx=70, pady=20, bg="#e42d25", fg="black",
font=Btn_text, border=10,command=tell_joke).place(x=610, y=580)#button for joke

quit_button = Button(root, text="Quit", padx=70, pady=20, bg="#e42d25", fg="black", font=Btn_text, border=10,
                     command=quit_app)#button for the window to end
quit_button.place(x=1000, y=580)

root.mainloop()
