# 310 Assignment3 ChatBot

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
### A3 New Features

* Add a new Graphical User Interface
* Add a new topic about movie
* When user input is out of scope chatbot will have various response
* Insensitive to word formation and synonyms
* Handle spelling mistakes
* Online chatting via Sockets


1. GUI
The GUI is build by puthon Tkinter. GUI will display the time of each message and user can check the history of the conversation on GUI.
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/GUI1.png)


2.New tpoic
Now user can have conversation with chatbot about movie. like movie name, movie character.
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/movie.png)


3.Various response
Now chatbot have various response when a input is out of scope. 
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/out%20of%20scope.png)


4.Insensitive to word formation and synonyms
In this chatbot, the WordNetLemmatizer in nltk is used to reduce inflected words to their stem or synonym like "run" and "running", "better" and "good".
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/lemmatizer.png)


5.Handle spelling mistakes
This chatbot use sklearn library to convert the input to a vector and compare the cosine similarity with the sentences in our corpus, so if the spelling mistakes are not obvious, it will not affect similarity checking.
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/spelling%20mistakes.png)


6.Online chatting via Sockets
Now user can use another computer to chat with the chatbot via sockets
Server
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/server2.png)
Client
![alt text](https://github.com/caincdiy/YueCao310/blob/GUI/readme_image/client2.png)

### How to use this program:
* Make sure training corpus and the program are in the same folder
* Run from command line `python server.py` first 
* Run Client and chat with chatbot.




