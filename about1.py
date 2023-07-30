from tkinter import *
import tkinter.messagebox
import contact1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()

    root.config(bg="white")
    root.title("Attendance System")
    root.geometry("700x500")
    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Home).pack()
    Label(root,text="").pack()
    """Button(root,text='About', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()
    Label(root,text="").pack()"""
    Button(root,text='Exit', height="1",width="20", bd=8, font=('Poppins', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    Message(root, text="Located in Kolkata, the state capital of West Bengal, Heritage Institute of Technology (HIT) is another prominent engineering and management institution. HIT was founded in 2001, is associated with the Maulana Abul Kalam Azad University of Technology (MAKAUT), and has a solid reputation for offering top-notch instruction in engineering and management fields. HIT provides a broad range of undergraduate and graduate degrees in disciplines like computer science, electronics and communication engineering, mechanical engineering, information technology, civil engineering, and more. The college's skilled teachers, cutting-edge facilities, and extensive educational offerings are well-known. In order to foster their general growth and development, it encourages students to take part in a range of extracurricular activities, workshops, and seminars.").pack()
    root.mainloop()
