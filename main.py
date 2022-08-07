from tkinter import *
import pyperclip
import random

window = Tk()
# window.geometry("280x300")
window.title("Pass Generator")
icon = PhotoImage(file="images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

def copy_button():
    psswd_entry = passwdEntry.get()
    pyperclip.copy(psswd_entry)

def generate():
    random_nums = random.randint(10000000,99999999999999)
    passwdEntry.delete(0, "end")
    passwdEntry.insert(0, random_nums)

Title = Label(window, 
                text="Поле з паролем: ", 
                font=("Cantarell", 14, "normal"), 
                fg="black", 
                bg="white")
Title.pack()

passwdEntry = Entry(window,
                font=("Cantarell", 10, "normal"))
passwdEntry.pack()

copy_button = Button(window,
                font=("Cantarell", 10, "normal"),
                command=copy_button,
                text="Copy")
copy_button.pack()

generate_button = Button(window,
                font=("Cantarell", 10, "normal"),
                command=generate,
                text='Generate')
generate_button.pack()

window.mainloop()