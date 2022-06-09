from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os


root = Tk()
root.title("Welcome to Tennis Ladder")
root.geometry('1024x768')
root.resizable(0,0)
bg = Image.open('background.jpg')
bg.thumbnail((1024, 768))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)

def new():
    if user_entry.get() == "":
        messagebox.showinfo("Login System", "Παρακαλώ δώστε όνομα χρήστη")
    elif password_entry.get() == "":
        messagebox.showinfo("Login System", "Παρακαλώ δώστε κώδικο")
    elif user_entry.get() == "" and password_entry.get() == "":
        messagebox.showinfo("Login System", "Παρακαλώ δώστε όνομα χρήστη και κώδικο")
    elif user_entry.get() == "admin" and password_entry.get() == "123":
        root.withdraw()
        paswd.set("")
        os.system('__main__.py')
        def home_page():
            new_window.withdraw()
            root.deiconify()
    else:
        messagebox.showinfo("Login System", "Λάθος στοιχεία εισόδου")
        paswd.set("")


canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=5)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
label = Label(root, text="Welcome to Tennis Ladder", font=('Tahoma 25 bold'), bg='grey', fg='white')
canvas.create_window(260, 40, anchor="nw", window=label)
user_label = Label(root, text="Χρήστης:", font=("Tahoma 18 bold"), bg='grey', fg='white').place(x=170, y=130)
canvas.create_window(140, 130, anchor="nw", window=user_label)
password_label = Label(root, text="Κωδικός:", font=("Τahoma 18 bold"), bg='grey', fg='white').place(x=170, y=200)
canvas.create_window(140, 210, anchor="nw", window=password_label)
user_entry = Entry(root, font=("Tahoma 18 bold"))
user_entry.focus()
canvas.create_window(290, 130, anchor="nw", window=user_entry)
paswd = StringVar()
password_entry = Entry(root, textvar=paswd, font=("Ariel 18 bold"), show="*")
canvas.create_window(290, 200, anchor="nw", window=password_entry)
login = Button(root, text="Έισοδος", font=("Tahoma 22 bold"),
            width=8, bg="grey", fg='#FFC331', relief=RAISED, cursor="hand2", command=new,borderwidth=2).place(x=290, y=250)
#login.pack(side=RIGHT, padx=15, pady=20)
canvas.create_window(290, 290, anchor="nw", window=login)
root.mainloop()