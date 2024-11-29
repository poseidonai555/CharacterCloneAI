from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests
import time

# AI functions
def message(character, message):
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

'''
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
'''

def read_characters_file():
    characters = {}
    count = 0
    with open(r'character_names.txt', 'r') as file:
        for line in file:
            count +=1
            characters[count] = line.strip()
    return characters

characters = read_characters_file()

for key in characters:
    print(f'{key} {characters[key]}')

while True:
    char_choice = input("Please enter a number for your character choice: ")
    try:
        character = characters[int(char_choice)]
    except:
        print("invalid input, must be one of the numbers assigned to the existing characters")
    else:
        break    

while True:
    user_message = input("~> ")
    if user_message == "exit":
        break
    else:
        print(message(character, user_message))