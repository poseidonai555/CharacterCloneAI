from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests

# button commands
def user_message(entry):
    message = entry.get()
    return message
def quit():
    window.destroy()
    global quit_GUI
    quit_GUI = True

# window protocols
def on_closing():
    messagebox.showwarning("Quit", "Use the end conversation button to close the application, or your conversation will not be saved!")

while True:
    quit_GUI = False
    window = Tk()
    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure('TButton', background='purple')
    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.title("Character name, chat history file name")
    window.configure(background="black")
    frame = Frame(window)
    frame.pack()
    message_entry = ttk.Entry(window)
    message_entry.pack()
    message_entry.bind("<Return>", lambda event: user_message(message_entry))
    quit_button = ttk.Button(window, text = "End conversation", command = quit)
    quit_button.pack()
    window.mainloop()
    if quit_GUI == True:
        break
