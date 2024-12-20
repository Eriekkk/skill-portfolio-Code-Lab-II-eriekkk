from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.font import Font
from functools import partial

root = Tk()#main window
root.title("Student Manager")#name of app
root.minsize(1500, 800)#size for window

bgclr = Label(root, bg='#f8f3f2')#background color for app
bgclr.place(x=0, y=0, relwidth=1, relheight=1)#fit the whole page 

Big_text = Font(family="Century Gothic", size=15, weight="bold")#setting font for big text
Btn_text = Font(family="Times New Roman Greek", size=10, weight="bold")#setting font for buttons
students = [] #containing student data 
student_data = 'C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt'#linkinhg the student data to python file

display_frame = Frame(root, bg='#f8f3f2')#display frame for the student data text
display_frame.place(x=80, y=50, width=900, height=700)#placing in the app

display = Text(display_frame, wrap=WORD, state='disabled', font=Big_text, bg='#f8f3f2', padx=10, pady=10, border=5)#student data text inside the display frame
display.pack(fill=BOTH, expand=True, padx=10, pady=10)#expnad to fit the display frame

title = Label(root, text="STUDENT MANAGER", font=Big_text, bg='#f8f3f2', fg='black')#the title of the app
title.place(x=500, y=10)#placing it on the middle top 



control_frame = Frame(root)#frame for the control buttons and student names 
control_frame.pack(side=RIGHT, fill=Y, padx=100, pady=10)#placing contro frame on the right


student_list_frame = LabelFrame(control_frame, text="Student lists", font=Big_text,  bg='#f8f3f2', fg="black")#student names inside the control frame
student_list_frame.pack(fill=BOTH, expand=True, pady=10)#playing the student names inside the control frame


def load_students(stdfile):#using function to load txt file in the pythong file
    global students#using global variable to work inside the function
    students = []  #reseting varaible
    with open(stdfile, 'r') as file: #reading all lines 
        file_lines = file.readlines()

    for line in file_lines[1:]:#ingorning the 10 in txt     
        if line.strip():#if statement for none empty lines
            split = line.strip().split(',')#splitting the lines when there is comma
            stdno = int(split[0])#student number
            stdname = split[1]#student name
            marks = list(map(int, split[2:5])) #work marks
            exam = int(split[5])#exam score
            total = sum(marks) + exam #total marks
            percentage = (total / 160) * 100 #calcuate the percentage variable
            grade = calculate_grade(percentage) #calculating the grade variable

            student = {#creating a dictionary
                    'code': stdno,
                    'name': stdname,
                    'work_marks': marks,
                    'exam_mark': exam,
                    'total_work': sum(marks),
                    'percentage': percentage,
                    'grade': grade
                }
            students.append(student)#adding all the data to the list 



def format_student(student):#the format when showing the data in dispaly function
    return (f"Name: {student['name']}\n"
            f"Student Number: {student['code']}\n"
            f"Total work Mark: {student['total_work']}\n"
            f"Exam Mark: {student['exam_mark']}\n"
            f"Overall Percentage: {student['percentage']:.2f}%\n"
            f"Grade: {student['grade']}\n\n")


def calculate_grade(percentage):#calculating the grade
    if percentage >= 70:#using if statements to calculate the grade 
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'


def save_student_data(filename, students):#saving student data in the file 
    with open(filename, 'w') as file:#openingg the filee 
        file.write(f"{len(students)}\n")#writing the total number of students
        for student in students:#using for loop to write all the student data 
            work = ','.join(map(str, student['work_marks']))
            file.write(f"{student['code']},{student['name']},{work},{student['exam_mark']}\n")


def display_records():#using function to display all the student data in the display function
        output = ""#using empty string to store data as a string


        for student in students:#using for loop to display all the student data
            formatted_student = format_student(student)
            output += formatted_student

        number_of_students = len(students)#counting the number of students 
        output += f"Number of Students: {number_of_students}\n"#displaying the number of students

        total_percentage = sum(student['percentage'] for student in students)#calculating the total percentage of each student
        average_percentage = total_percentage / number_of_students if number_of_students > 0 else 0 
        #calculating the average percentage

        output += f"Average Percentage: {average_percentage:.2f}%\n"#displaying the average percentage

        update_display(display, output)#calling and updating the text in the display

def update_display(text_widget, text):#using function to update the text in the display
    text_widget.config(state='normal')#enable display to show text 
    text_widget.delete(1.0, END)#clear display
    text_widget.insert(END, text)#adding text 
    text_widget.config(state='disabled')#disable the display

def view_specific_student(name, event=None):#using function to view a specific student data 
    student = None

    for stdname in students:#using for loop to find the specific student
        if stdname['name'] == name:#using if statement to find the specific student name and data 
            student = stdname  
            break  

    if student:#using if statement to check if the student is found
        student_info = format_student(student)#using function to format the student data
        
        update_display(display, student_info)#calling and updating the text in the display
    else:
        messagebox.showinfo("Not Found", f"Student with the name '{name}' was not found.")#displaying the message that the studetn is not found

def view_all_records():#using function to view all the student data
    display_records()#calling the function to show all the student data


def add_student():#using function to new student data 

        stdcode = simpledialog.askinteger("Add Student", "Enter Student ID:")#asking the user to add a new student id number
        if stdcode is None:#using if statement to check if the student id is none
            return 

        if any(student['code'] == stdcode for student in students):#using for loop to check if the student id already exists withing the data
            messagebox.showerror("Duplicate ID", "A student with this ID already exists.")#displaying the message if the id already exist
            return

        stdname = simpledialog.askstring("Add Student", "Enter Student Name:")#asking the user to add a new student name
        if not stdname:
            messagebox.showerror("Invalid Input", "Student name cannot be empty.")#displaying the message if the user leaves it empty
            return
        marks = []#storing marks to add new data 
        for i in range(3):#using for loop to add and ask user for 3 times for the marks
            mark_input = simpledialog.askinteger("Add Student", f"Enter work Mark {i + 1} (out of 20):")#asking user for the work marks
            if mark_input is None or not (0 <= mark_input <= 20):#if statement to make sure the number is between 0 and 20
                messagebox.showerror("Invalid Input", "Work mark must be between 0 and 20.")#if not between 0 to 20 message will display
                return
            marks.append(mark_input)#adding the users input into the empty list 


        exam = simpledialog.askinteger("Add Student", "Enter Exam Mark (out of 100):")#asking user for their exam mark
        if exam is None or not (0 <= exam <= 100):#if statement to make sure the number is between 0 and 100
            messagebox.showerror("Invalid Input", "Exam mark must be between 0 and 100.")#if not between 0 to 100 message will display
            return


        total_work = sum(marks)#storing and adding the sum of 3 marks
        percentage = (total_work + exam) / 160 * 100 #calculating the percentage of the new given data
        grade = calculate_grade(percentage)#calling function to calculate the grade while storing it


        student = {#storing the new student data to the dictionary
            'code': stdcode,
            'name': stdname,
            'work_marks': marks,
            'exam_mark': exam,
            'total_work': total_work,
            'percentage': percentage,
            'grade': grade
        }
        students.append(student)#the student dictionary storing it in the student list


        save_student_data("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt", students)#updating the txt file

    
        lbl = Label(student_list_frame, text=student['name'], fg="black", cursor="hand2")#adding the new studetent name in the student list
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", partial(view_specific_student, student['name']))

        messagebox.showinfo("Success", "Student added successfully!")#displaying the message when the student is added and successfull
        display_records()  #displaying all the student data including the new one




def delete_student(): #function to delete all student data 
    stdcode = simpledialog.askinteger("Delete Student", "Enter Student ID to delete:")#asking the user to enter a student id to delete
    if stdcode is None:#using if statement to check if the student id is none
        return  

    student_found = False # new variable to check if the student is found 
    for i, student in enumerate(students):#using for loop to find a student with the given id 
        if student['code'] == stdcode:#using if statement to find a student and delete it
            del students[i]
            student_found = True
            for widget in student_list_frame.winfo_children():
                if widget.cget("text") == student['name']:
                    widget.destroy()
                    break


            save_student_data("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt", students)#updating the list in the txt file

            messagebox.showinfo("Success", f"Student with ID {stdcode} deleted successfully!")#displaying the message when the student data is deleted
            display_records() 
            return

    if not student_found:
        messagebox.showerror("Error", f"No student found with ID {stdcode}.")#when no student is id is found this message is shown

def update_student():#using function to update student data
    stdname = simpledialog.askstring("Update Student", "Enter Student Name:")#asking user for student name
    
    student = None#another student function

    for s in students:#another loop to find the specific name
        if s['name'] == stdname:
            student = s 
            break 

    if student:#another if statement to check if the student is found
        marks = []#empty list to store updated marks
        for i in range(3):#using for loop to update the new student marks
            mark_input = simpledialog.askinteger("Update Student", f"Enter New work Mark {i + 1} (out of 20):")#asking user for new marks
            if mark_input is not None and 0 <= mark_input <= 20:#if statement to check if it's between 0 to 20
                marks.append(mark_input)#adding marks to marks list
            else:
                messagebox.showerror("Invalid Input", "Coursework mark must be between 0 and 20.")#showing if not between 0 to 20
                return  


        exam = simpledialog.askinteger("Update Student", "Enter New Exam Mark (out of 100):")#asking user for new exam mark
        if exam is None or not (0 <= exam <= 100):#check if its between 0 or 100
            messagebox.showerror("Invalid Input", "Exam mark must be between 0 and 100.")#if not between 0 to 100
            return 
        
        #updating the student list
        student['work_marks'] = marks
        student['exam_mark'] = exam
        
        student['total_work'] = sum(marks)
        student['percentage'] = (sum(marks) + exam) / 160 * 100
        

        student['grade'] = calculate_grade(student['percentage'])

        save_student_data("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt", students)#saving new data to txt file


        messagebox.showinfo("Success", "Student updated successfully!")
        

        display_records()
    else:

        messagebox.showinfo("Not Found", f"Student with the name '{stdname}' not found.")

def sort_students(order):#using function to sort the student data ascending or descending
    descending = (order == "desc")#using descending variable to check if its descending

    global students
    students = sorted(students, key=lambda student: student['percentage'], reverse=descending)#using sorted function to sort data ascending or descending

    display_records()#show all student data with the new ordeer

allrecs = Button(control_frame, text="View All Records", font=Btn_text, bg="#16517d", fg="white", border=10, padx=50, command=lambda: view_all_records()).pack(pady=5)#button to show all student data
asc = Button(control_frame, text="Sort Ascending", font=Btn_text, bg="#16517d", fg="white", border=10, padx=55, command=lambda: sort_students("asc")).pack(pady=5)#button to sort data ascneding
desc = Button(control_frame, text="Sort Descending", font=Btn_text, bg="#16517d", fg="white", border=10, padx=50, command=lambda: sort_students("desc")).pack(pady=5)#button to sort data descending
addstd = Button(control_frame, text="Add Student", font=Btn_text, bg="#16517d", fg="white", border=10, padx=62, command=add_student).pack(pady=5)#button to add student data
deletestd = Button(control_frame, text="Delete Student", font=Btn_text, bg="#16517d", fg="white", border=10, padx=54, command=delete_student).pack(pady=5)#button to delete student data
updatestd = Button(control_frame, text="Update Student", font=Btn_text, bg="#16517d", fg="white", border=10, padx=53, command=update_student).pack(pady=5)#button to update student data


load_students("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt")#loading all the student data in the txt file while calling the function





for student in students:#loop to show all student name in the student list frame
    lbl = Label(student_list_frame, text=student['name'], fg="black", cursor="hand2")#text
    lbl.pack(anchor="w", padx=5, pady=2)#placing student names
    lbl.bind("<Button-1>", partial(view_specific_student, student['name']))#partial function to call show spedific student 
    #button 1 is left mouse button click

root.mainloop()
