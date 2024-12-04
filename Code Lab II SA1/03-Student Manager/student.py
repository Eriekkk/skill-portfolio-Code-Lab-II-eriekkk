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


def add_student():#using function to add a new student data
        stdcode = simpledialog.askinteger("Add Student", "Enter Student ID:")#using simpledialog to ask user for student id
        stdname = simpledialog.askstring("Add Student", "Enter Student Name:")#asking user for student name
        marks = [simpledialog.askinteger("Add Student", f"Enter work Mark {i+1} (out of 20):") for i in range(3)]#asking user for work marks
        exam = simpledialog.askinteger("Add Student", "Enter Exam Mark (out of 100):")#asking user for exam mark

        student = {#storing new student data in the student dictionary
            'code': stdcode,
            'name': stdname,
            'work_marks': marks,
            'exam_mark': exam,
            'total_coursework': sum(marks),
            'percentage': (sum(marks) + exam) / 160 * 100,
            'grade': calculate_grade((sum(marks) + exam) / 160 * 100)
        }
        students.append(student)#adding the new student data to the list 
        
        save_student_data("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt", students)#saving the new student data to the txt file
        messagebox.showinfo("Success", "Student added successfully!")#showing the message that it was sucessfull
        display_records()#calling function to show all the student data with the new data
        lbl = Label(student_list_frame, text=student['name'], fg="black", cursor="hand2")
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", partial(view_specific_student, student['name'])) 


def delete_student():#a function to delete student data
    name = simpledialog.askstring("Delete Student", "Enter Student Name:")#using simpledialog to ask user for student name to delete
    

    student_found = False#using student found variable to check if the student is found
    
    global students#using global variable to work inside the function
    updated_students = []#using empty list to store the updated student data
    
    for student in students:#using for loop to check if the student is found
        if student['name'] == name:#using if statement to check if the student is found
            student_found = True 
        else:
            updated_students.append(student)  
    students = updated_students#updating the student data
    
    save_student_data("C:/Users/eriel/Desktop/Code Lab II SA1/03-Student Manager/studentMarks.txt", students)#saving the deleted student data in the txt file
    
    if student_found:#using if statement to check if the student is found
        messagebox.showinfo("Success", "Student deleted successfully!")#if found message
    else:
        messagebox.showinfo("Not Found", f"Student with the name '{name}' not found.")#if not found message
    
    display_records()#calling function to show all the student data with the deleted function
    delete()#calling fucntion to delete student data and to refresh the student list


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


def delete():#using function to delete student data and to refresh the student list
    for widget in student_list_frame.winfo_children():#for loop to destroy all the widgets
        widget.destroy()#destroying all the widgets previously used
    


for student in students:#loop to show all student name in the student list frame
    lbl = Label(student_list_frame, text=student['name'], fg="black", cursor="hand2")#text
    lbl.pack(anchor="w", padx=5, pady=2)#placing student names
    lbl.bind("<Button-1>", partial(view_specific_student, student['name']))#partial function to call show spedific student 
    #button 1 is left mouse button click

root.mainloop()
