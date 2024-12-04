from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import random

root = Tk()#main window
root.title("Math Quiz")#name of app
root.minsize(1500, 800)#size for window

current_question = 0 #variable to keep track on the current question number
score = 0 #variable to keep track on the score
difficulty = "" #variable to keep track on the difficulty
attempts = 0 #variable to keep track on the number of attempts
problems = {} #dictionary to store the questions 
Big_text = Font(family="Century Gothic", size=50, weight="bold")#font for big text
Small_text = Font(family="Century Gothic", size=20, weight="bold")#font for small text
Btn_text = Font(family="Times New Roman Greek", size=20, weight="bold")#font for buttons

bgimg = "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/starting.png" #linking the image in python
orgimg = Image.open(bgimg).resize((1500, 800)) #resizing the image
startbg = ImageTk.PhotoImage(orgimg) #placing the image as the background

start_frame = Frame(root) #frame for the starting screen of the quiz
start_frame.pack(fill=BOTH, expand=True) #placing the starting screen

end_frame = Frame(root)#frame for the end screen of the quiz
end_frame.pack(fill=BOTH, expand=True)#placing the end screen

startimg = Label(start_frame, image=startbg)
startimg.pack(fill=BOTH, expand=True)#plainc the background image

mq = Label(start_frame, text="MATH QUIZ", font=Big_text, bg="white", fg="black").place(x=560, y=250)#math quiz text in the startin screen
def show_menu():#function to transition to menu page
    start_frame.pack_forget()#hiding the starting screen
    menu()#caling menu function

startbtn = Button(start_frame,text="START",font=Btn_text,bg="#ffcc00",fg="black",padx=70, pady=20,
    border=10,command=show_menu,).place(x=630, y=630)#start button for the starting screen

# Menu screen
def menu():#function for menu page
    global menu_frame#global variable to work in the function
    menu_frame = Frame(root)#frame for the menu frame
    menu_frame.pack(fill=BOTH, expand=True)#placing the menu frame in the window

    bg_img = "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/diff.png"#linking the menu image 
    bg_image = Image.open(bg_img).resize((1500, 800))#resizing the menu image
    bg_label = ImageTk.PhotoImage(bg_image)

    bg = Label(menu_frame, image=bg_label)
    bg.image = bg_label
    bg.pack(fill=BOTH, expand=True) #placing the menu image

    Label(menu_frame, text="DIFFICULTY LEVEL", font=Big_text, bg="white", fg="black").place(x=470, y=70)#text for the menu

    Easybtn = Button(menu_frame, text="EASY", font=Btn_text, bg="green", fg="white", padx=70, pady=20,  border=10,
           command=lambda: show_level_page("easy")).place(x=630, y=250)#easy button
    Moderatebtn = Button(menu_frame, text="MODERATE", font=Btn_text, bg="orange", fg="white", padx=30, pady=20,  border=10,
           command=lambda: show_level_page("moderate")).place(x=630, y=400)#moderate button
    Hardbtn = Button(menu_frame, text="HARD", font=Btn_text, bg="red", fg="white", padx=70, pady=20,  border=10,
           command=lambda: show_level_page("hard")).place(x=630, y=550)#hard button


def show_level_page(level):#function to transition to level page
    global difficulty#global variable to work in the function
    difficulty = level#assigning difficulty level
    menu_frame.pack_forget() #hiding the menu frame
    start_quiz()#calling start quiz function which starts the quiz


def number_generator(level):#function to generate random numbers 
    if level == "easy":#using if statement to check the level and generate random numbers for specific level
        return random.randint(1, 9)
    elif level == "moderate":
        return random.randint(10, 99)
    elif level == "hard":
        return random.randint(1000, 9999)


def operation_generator():#function to generate either addition or subtraction equation
    return random.choice(["+", "-"])


def question_generator(level):#function to generate a question in the quiz
    num1 = number_generator(level)#storing the number generator function in num1
    num2 = number_generator(level)#storing the number generator function in num2
    operation = operation_generator()#storing the operation generator function
    return f"{num1} {operation} {num2}"#returning the question with f string to combine the numbers and operation


def start_quiz():#function to start the quiz
    global current_question, score, problems#global variable to work in the function
    current_question = 0 #reseting variable
    score = 0 #reseting variable
    problems = {#dictionary to store the questions and generating 10 questions with if statement
        f"Q{i+1}": question_generator(difficulty) 
        for i in range(10)
        }

    show_quiz()#calling show quiz function

def show_quiz():#function to show the quiz questions and widgets
    global current_question, problems, score, attempts, submit_button#global variable to work in the function

    attempts = 0  #reseting variable

    quiz_frame = Frame(root)#frame for the quiz
    quiz_frame.pack(fill=BOTH, expand=True)#placing the quiz


    level_bg = {#dictionary to store background for specific level or difficulty
        "easy": "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/easybg.png",
        "moderate": "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/moderatebg.png",
        "hard": "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/hardbg.png",
    }

    bg_image = Image.open(level_bg[difficulty]).resize((1500, 800))#resizing the background image
    bg_label = ImageTk.PhotoImage(bg_image)#placing the background image

    bg = Label(quiz_frame, image=bg_label)#placing the background image
    bg.image = bg_label#placing the background image
    bg.pack(fill=BOTH, expand=True)#placing the background image

    level_label = Label(quiz_frame, text=f"Level: {difficulty.capitalize()}", font=Small_text, bg="white", fg="black")#text for level
    level_label.place(x=65, y=30)#placing the text

    question_label = Label(quiz_frame, text=f"Question: {current_question + 1}/10", font=Small_text, bg="white", fg="black")#text for currenct question number
    question_label.place(x=620, y=30)

    score_label = Label(quiz_frame, text=f"Score: {score}", font=Small_text, bg="white", fg="black")#text for current score
    score_label.place(x=1180, y=30)

    problem_label = Label(quiz_frame, text=f"What is {problems[f'Q{current_question + 1}']}?", font=Big_text, bg="white", fg="black")#text for the question
    problem_label.place(x=500, y=155)

    answer = Entry(quiz_frame, font=("Arial", 20), width=20, border=10, justify="center")#asking the user to enter an answer
    answer.place(x=600, y=500)

    feedback_label = Label(quiz_frame, text="", font=Big_text, bg="white", fg="red")#text if the user need to try again
    feedback_label.place(x=320, y=370)

    def check_answer():#function to check if the answer is correct
        global score, attempts#global variable to work in the function
        user_answer = int(answer.get())#getting from the answer variable and switching from string to integer
        correct_answer = eval(problems[f"Q{current_question + 1}"])#evaluating the correct answer and storing it

        if user_answer == correct_answer:#if statement to check the correct answer
            feedback_label.config(text="Correct!", fg="green")#text if the answer is correct
            score += 10#add 10 points to the score
            show_next_question()#calling show next question function to go to next question
        else:
            attempts += 1#add 1 to the attempts
            if attempts == 1:#if statement to check the number of attempts
                feedback_label.config(text="Wrong Answer!!! Try again!!!!", fg="orange")#text if the answer is wrong and you need to try again
            else:
                feedback_label.config(text="Wrong! Moving to next question.", fg="red")#text if the answer is wrong again 
                show_next_question()#calling show next question function to go to next question

    def show_next_question():#function to show the next question when it's answered 
        global current_question, attempts#global variable to work in the function
        current_question += 1#add 1 to the current question
        attempts = 0  #reseting variable

        if current_question < 10:#if statement to check the number of questions if its more than 10 question it will end the quiz
            problem_label.config(text=f"What is {problems[f'Q{current_question + 1}']}?")#text for the question
            question_label.config(text=f"Question: {current_question + 1}/10")#text for currenct question number
            score_label.config(text=f"Score: {score}")#text for current score
            feedback_label.config(text="")#clearning the feedback text
            answer.delete(0, END)#clearning the answer
        else:
            end_quiz()#calling end quiz function to show score

    submit_button = Button( quiz_frame,text="SUBMIT",font=Btn_text, bg="black",fg="white",
    padx=40,pady=15,border=10,command=check_answer,).place(x=650, y=620)#submit button

    def end_quiz():#function for the end of the quiz
        global end_frame #global variable to work in the function
        for widget in root.winfo_children(): #for loop to destroy all the widgets
             widget.destroy()#destroying all the widgets previously used

        end_frame = Frame(root)#frame from for the end screen
        end_frame.pack(fill=BOTH, expand=True)#placing the end screen

        end_bg_image = "C:/Users/eriel/Desktop/Code Lab II SA1/01- MathQuiz/Image/scorepng.png"#link the end image
        end_bg = Image.open(end_bg_image).resize((1500, 800))
        end_bg_label = ImageTk.PhotoImage(end_bg)


        end_bg_label_widget = Label(end_frame, image=end_bg_label)
        end_bg_label_widget.image = end_bg_label
        end_bg_label_widget.pack(fill=BOTH, expand=True)


        result_label = Label(end_frame, text=f"Quiz Over! Your Score: {score}/100", font=Big_text,
         bg="white", fg="black").place(x=320, y=250)#text to show the total score of the user


        backbtn = Button(end_frame, text="BACK TO MAIN MENU", font=Btn_text, bg="#2a60bb", fg="white",border=10, padx=50,
         command=go_back_to_start).place(x=550, y=400)#button to go back to the level menu



def go_back_to_start():#function to go back to the start screen
    
    for widget in root.winfo_children():#for loop to destroy all the widgets
        widget.destroy()#destroying all the widgets previously used

    show_menu()#calling show menu function to go back to the menu



root.mainloop()
