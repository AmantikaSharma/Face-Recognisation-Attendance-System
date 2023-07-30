from tkinter import *
import tkinter.messagebox
import about1
import contact1
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageFont


def Register():
    global root
    root.destroy()
    import index





def Home():
    global root
    root.destroy()
    main_display()
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()

def Detail():
    global root
    root.destroy()
    import details

def Attandance():
    global root
    root.destroy()
    import check
def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()
    root.config(bg="#575556")
    root.title("Face Recognition Based Attendance System")
    root.geometry("700x500")



    custom_font_path = "/Pop.ttf"  # Replace with the actual path to your font file

    try:
        custom_font = ImageFont.truetype(custom_font_path, size=20)
    except OSError as e:
        # print(f"Error loading the custom font: {e}")
        custom_font = None  # Fallback to the default font if the custom font cannot be loaded

    # Define a callback function for the buttons
    def on_button_click():
        print("Button clicked!")

    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=("Poppins", 15, 'bold'), fg="white",
                   bg="#575556",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
                   bg="blue", command=Home).pack()
    Label(root, text="").pack()
    Button(root, text='Register', height="1", width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=Register).pack()
    Label(root,text="").pack()
    Button(root, text='Take Attandance', height="1", width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove",
           fg="white", bg="blue", command=Attandance).pack()
    Label(root, text="").pack()
    #Button(root, text='Detail', height="1", width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
           #bg="blue", command=Detail).pack()#
    Button(root,text='About', height="1",width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=4, font=("Poppins", 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    Label(root,text="").pack()
    root.mainloop()

main_display()
