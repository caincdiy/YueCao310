# -*- coding: utf-8 -*-
"""
Created on Wed Mar 3rd 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: yue cao 59468165  whq 672437089
"""
import generateResponse as gr
import preprocess as pp

content = ""
with open("corpus.txt") as infile:
    for line in infile:
        content = content + " " + line.lower()
qrDict = pp.generateConversationTurnDict(content)
index = 0


'''
for question,answer in qrDict.items():
    print("question is:"+question+', answer is'+answer+', index is:'+str(index))
    index+=1
'''

pureQuestions = pp.pureQuestionsText(qrDict)
sentenceTokens = pp.generateSentenceTokens(pureQuestions)
index2 = 0


'''

for question in sentenceTokens:
    print("index is:"+str(index2)+", question is:"+question)
    index2+=1'''
ql = []
for question, response in qrDict.items():
    ql.append(question)
#print(sentenceTokens)
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






