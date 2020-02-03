from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"how are you ?|how are u ?",
        ["I'm doing good \n How about You ?", ]
    ],
    [
        r"i'm (.*) doing (.*)|i am (.*) doing (.*)",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"what is your name ?|what's your name ?",
        ["I am FREDDY the CHATBOT. \n You ?", ]
    ],
    [
        r"(my name is|i'm|i am) (.*)",
        ["Hello %2, that's nice.", ]
    ],
    [
        r"thank you (.*)|thank you",
        ["Your welcome" ]
    ],
    [
        r"(.*) created ?",
        ["Mastermind", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya-Pradesh', ]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",]
    ],
    [
        r"quit|good bye|bbye|ok bye",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


import tkinter as tk
from PIL import ImageTk, Image

master = tk.Tk()
def ask():
    query=textF.get()
    chat=Chat(pairs, reflections)
    answer=chat.respond(query)
    msg.insert(tk.END, "You : " +query)
    msg.insert(tk.END, "Freddy : " + answer)
    textF.delete(0,tk.END)
    
def userText(event):
    textF.delete(0,tk.END)
    
    
master.title("ChatBot")
master.geometry("500x900")
img=ImageTk.PhotoImage(Image.open(r"C:\Users\akash\Desktop\bot.png"))
photo=tk.Label(master, image=img,width=220,height=180)
photo.grid(column=1,row=1)
photo.pack(pady=10)

master.configure(bg='lightgrey')
frame=tk.Frame(master)
sc=tk.Scrollbar(frame)
msg=tk.Listbox(frame, width=80, height=25,fg='black')
msg.configure(bg='white')
sc.pack(side=tk.RIGHT, fill=tk.Y)
msg.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)
frame.pack()
textF=tk.Entry(master, font=("Verdana", 12),fg='dimgrey',bg="#E0FFFF",width=25)
textF.insert(1,"Start conversation here")
textF.bind("<Button>",userText)
textF.pack(pady=20)
button =tk.Button(master,
                   text="Enter",
                   fg="blue",
                   command=ask)
button.pack()
master.mainloop()
