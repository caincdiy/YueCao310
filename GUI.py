
from tkinter import *
import time



def sendmessage():
    mes=getline()
    content = 'me ' + time.strftime('%Y-%M-%D %H:%M:%S', time.localtime()) + '\n'
    text_list.insert(END, content, 'sendcolor')
    text_list.insert(END, mes)
    replay = res(mes)
    getmessage(replay)


def getmessage(replay):
    content = 'chatbot ' + time.strftime('%Y-%M-%D %H:%M:%S', time.localtime()) + '\n'
    text_list.insert(END, content, 'rescolor')
    text_list.insert(END, replay)
    text_list.see(END)

def getline():
    mes = text_sent.get('0.0', END)
    text_sent.delete('0.0', END)
    return mes

def enter(event=None):
    sendmessage()






root = Tk()
root.title("chatbot")
root.geometry("500x500")
frm_output = Frame(root, width=500, height=300)
frm_input = Frame(root, width=500, height=150)
frm_button = Frame(root, width=500, height=50)
text_list = Text(frm_output)
text_list.tag_configure('sendcolor', foreground='green')
text_list.tag_configure('rescolor', foreground='blue')
text_sent = Text(frm_input)
send = Button(frm_button, text='Send', font=10, command=sendmessage)
text_sent.bind('<Return>', enter)
frm_output.propagate(0)
frm_output.grid(row=0, column=0)
frm_input.propagate(0)
frm_input.grid(row=1, column=0)
frm_button.propagate(0)
frm_button.grid(row=2, column=0)
send.pack()
text_list.pack()
text_sent.pack()

def buildUI():
    root.mainloop()

buildUI()