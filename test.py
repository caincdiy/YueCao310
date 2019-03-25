# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:39:24 2019

@author: whq672437089
"""
'''
import unittest 
import preprocess as pp

class testPreprocess(unittest.TestCase):
    def setUp(self):
        self.content="- - what is the illuminati \n - secret - - what is vineland \n - novel"
        self.template={"what is the illuminati":" secret","what is vineland":" novel"}
        self.question="what is  illuminati .\n what is vineland .\n "
    
    def tearDown(self):
        del self.content
        del self.template
    
    def testGenerateConversationTurnDict(self):
        self.assertTrue(self.template==pp.generateConversationTurnDict(self.content))
        
    def testPureQuestionText(self):
        self.assertTrue(self.question==pp.pureQuestionsText(self.template))
        
def mySuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testPreprocess))
    return suite

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(mySuite())
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 3rd 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: yue cao 59468165
"""
'''
import generateResponse as gr
import preprocess as pp
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


def res(input1):
    st = ""
    # userInput = input()
    input1 = pp.sanitize_questions(input1.lower())
    if (input1 != 'bye'):
        if (input1 == 'thanks' or input1 == 'thank you'):
            # print("ROBO: You are welcome..")
            return "You are welcome.." + '\n'
        else:
            # print("ROBO: "+gr.generateResponse(userInput,sentenceTokens,qrDict,ql))
            st = gr.generateResponse(input1, sentenceTokens, qrDict, ql) + '\n'
            sentenceTokens.remove(input1)
            return st
    else:
        # print("ROBO: Bye! take care..")
        return "Bye! take care.." + '\n'


content = ""
with open("corpus.txt") as infile:
    for line in infile:
        content = content + " " + line.lower()
qrDict = pp.generateConversationTurnDict(content)
index = 0




for question,answer in qrDict.items():
    print("question is:"+question+', answer is'+answer+', index is:'+str(index))
    index+=1


pureQuestions = pp.pureQuestionsText(qrDict)
sentenceTokens = pp.generateSentenceTokens(pureQuestions)
index2 = 0

for question in sentenceTokens:
    print("index is:"+str(index2)+", question is:"+question)
    index2+=1
ql = []
for question, response in qrDict.items():
    ql.append(question)

'''

"""


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
"""