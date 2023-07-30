from tkinter import *
import tkinter.messagebox

import about1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("700x500")
    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Home).pack()
    """Label(root,text="").pack()
    Button(root,text='About', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()"""
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    var="""
    
1
Amantika Sharma	
Mobile: +91 81015 42798
E-mail: amantika.sharma.aeie24@heritageit.edu.in
College: Heritage Institute of Technology - Kolkata - 700107
Department: Applied Electronics & Instrumentation Engineering
Roll No: 2053016

2
Ayush Anand	
Mobile: +91 99557 15950 
E-mail: ayush.anand.aeie24@heritageit.edu.in
College: Heritage Institute of Technology - Kolkata - 700107
Department: Applied Electronics & Instrumentation Engineering
Roll No: 2053016

"""
    Message(root,text=var,width="1500").pack()
    root.mainloop()

