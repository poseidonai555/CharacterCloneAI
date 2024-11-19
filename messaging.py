from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests
import time

# AI functions
def message(character, message, message_count, last_message_count):
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": character,
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    character_response = response.json()['choices'][0]['message']
    return character_response


# window protocols
def on_closing():
    messagebox.showwarning("Quit", "Use the end conversation button to close the application, or your conversation will not be saved!")

# Global variables
character = "Assistant"
message_count = 0
last_message_count = 0

# GUI functions
def on_closing():
    messagebox.showwarning("Quit", "Use the quit program button to close the application, so that your chat history is saved")
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
def quit():
    window.destroy()

window = Tk()
style = ttk.Style(window)
style.theme_use("clam")
style.configure('TButton', background='purple')
window.protocol("WM_DELETE_WINDOW", on_closing)
window.title("history name + character")
window.configure(background='black')
frame = Frame(window)
frame.pack()
user_message = ttk.Entry(window, )
QUIT_button = ttk.Button(window, text = "Quit program", command=quit)
QUIT_button.pack()
window.mainloop()