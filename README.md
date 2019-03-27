# 310 ChatBot

### Team Member: 

Yue Cao, ALex Qin, Yuqi Sun, Haoqiu Wu, Michael Wu
###Individual part:
Yue Cao

### Introduction: 

This is a simple chatbot program. The most fundamental theory that this program relies on is text similarity. 

The following steps decribe the logic of chatbot program:
* Clean text, including remove punctuation, duplicate whitespace.
* Divide text into multiple independent conversaiton turns.
* Based on such conversation turns, create a dictionary whose key is the question and value is the response.
* Combine only questions, then tokenlizing and lemmatization them.
* Vectorize those sentence tokens and compare the user input with them.
* Find the most similar question and use it as key to retrieve answer from training corpus.
* Output answer/response.
GUI will take input from user and print the input on the UI, then send the message to the server. server will take the message 
and get response from chatbot then send the answer back, and GUI will print the message on UI.

The training corpus used in our project comes from this [Repo](https://github.com/gunthercox/chatterbot-corpus)

### How to use this program:
* Make sure training corpus and the program are in the same folder
* Run from command line `python server.py` first 
* Run Client and chat with chatbot.

(https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/GUI.png)


