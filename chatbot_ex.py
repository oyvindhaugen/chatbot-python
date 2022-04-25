import chatbot as c
from tkinter import *
import random

def main():
    x = c.ent_message.get().lower().split()
    print(x)
    if 'what' in x:
        y = x.index('what')
        # what as first index of the list
        if y == 0:
            if 'string' in x:
                c.txt_history.insert(END, "\nBot-> A string is a collection of characters.")
            elif 'integer' in x:
                c.txt_history.insert(END, "\nBot-> An integer is a whole number.")
            elif 'float' in x:
                c.txt_history.insert(END, "\nBot-> A float is a number with decimals.")
            elif 'list' in x:
                c.txt_history.insert(END, "\nBot-> A list is an ordered sequence of elements.")
            elif 'tuple' in x:
                c.txt_history.insert(END, "\nBot-> A tuple stores multiple items in one variable.")
            elif 'set' in x:
                c.txt_history.insert(END, "\nBot-> A set stores multiple items in one variable")
            elif 'boolean' in x:
                c.txt_history.insert(END, "\nBot-> A boolean returns a true or false value.")
            elif 'bool' in x:
                c.txt_history.insert(END, "\nBot-> A boolean returns a true or false value.")
            elif 'python' in x:
                if 'libaries' in x:
                    c.txt_history.insert(END, "\nBot-> Other Python GUI Libaries include PyQt, PySide, Kivy and wxPython.")
                elif 'library' in x:
                    c.txt_history.insert(END, "\nBot-> Other Python GUI Libaries include PyQt, PySide, Kivy and wxPython.")
                c.txt_history.insert(END,
                                     "\nBot-> Python is a high level general-purpose programming language. It has indent syntax and is highly loved by many. It was created in 1991 by Guido van Rossum.")
            elif 'life' in x:
                c.txt_history.insert(END, "\nBot-> 42")
            elif 'function' in x:
                c.txt_history.insert(END,
                                     "\nBot-> A function is a collection of code that gets executed when it's called.")
            elif 'tello' in x:
                c.txt_history.insert(END,
                                     "\nBot-> Tello is a Python library you can use to program Tello drones.")
            elif 'variable' in x:
                if 'name' in x:
                    c.txt_history.insert(END, "\nBot-> The best way to name your variable is by giving it a fitting and describing name. You can for example name a list of animals 'my_animals'.")
                else:
                    c.txt_history.insert(END, "\nBot-> A variable is a way to store data.")
            elif 'tkinter' in x:
                c.txt_history.insert(END, "\nBot-> Tkinter is a library used to create a Graphical User Interface (GUI) for Python apps.")
            elif 'gui' in x:
                c.txt_history.insert(END, "\nBot-> A GUI is a Graphical User Interface which makes it so you don't have to write and read in command line.")
            elif 'food' in x:
                c.txt_history.insert(END, "\nBot-> My favorite food is a good serving of megabytes and a pint of electricity! :D")
            else:
                c.txt_history.insert(END,
                                     "\nBot-> Please ask the question again in a different way or ask something else.")
    elif 'how' in x:
        y = x.index('how')
        # how as first index of the list
        if y == 0:
            if 'string' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a string by putting characters inside quotation marks 'like this'.")
            elif 'integer' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make an integer by putting a whole number as the value of the variable, like this: x=3.")
            elif 'float' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a float by putting a number with decimals as the value of the variable, like this: x:3.14.")
            elif 'list' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a list by putting the value of the variable as: animals = ['dog', 'cat' 'fish'].")
            elif 'tuple' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a tuple by putting the value of the variable as: animals = ('dog', 'cat', 'fish').")
            elif 'set' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a set by putting the value of the variable as: animals = {'dog', 'cat', 'fish'}.")
            elif 'boolean' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a boolean by putting the value of the variable as: x = true.")
            elif 'bool' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make a boolean by putting the value of the variable as: x = true.")
            elif 'tello' in x:
                c.txt_history.insert(END,
                                     "\nBot-> You can make it takeoff with the .takeoff() function, make it fly forward with .move_forward() function, and make it land with the .land() function.")
            elif 'variable' in x:
                c.txt_history.insert(END, "\nBot-> You can write a variable by using a value like a string or an integer. You can do it like this: x = 'I am a bot'.")
            elif 'you' in x:
                c.txt_history.insert(END, "\nBot-> I am good, but I do hope you're better! What can I help you with?")
            elif 'you?' in x:
                c.txt_history.insert(END, "\nBot-> I am good, but I do hope you're better! What can I help you with?")
            else:
                c.txt_history.insert(END,
                                     "\nBot-> Please ask the question again in a different way or ask something else.")
    elif 'thank you' in x:
        c.txt_history.insert(END, "\nBot-> No problem! Is there anything else I can help you with?")
    elif 'bye' in x:
        y = random.randint(0, 3)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> I'll talk to you later then!")
        elif y == 1:
            c.txt_history.insert(END, "\nBot-> Thanks for asking me! Have a great day and I hope I helped you something!")
        elif y == 2:
            c.txt_history.insert(END, "\nBot-> It was great talking to you! Good luck coding!")
        else:
            c.txt_history.insert(END, "\nBot-> You can do it champ!")
    elif 'goodbye' in x:
        y = random.randint(0, 3)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> I'll talk to you later then!")
        elif y == 1:
            c.txt_history.insert(END, "\nBot-> Thanks for asking me! Have a great day and I hope I helped you something!")
        elif y == 2:
            c.txt_history.insert(END, "\nBot-> It was great talking to you! Good luck coding!")
        else:
            c.txt_history.insert(END, "\nBot-> You can do it champ!")
    elif 'cya' in x:
        y = random.randint(0, 3)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> I'll talk to you later then!")
        elif y == 1:
            c.txt_history.insert(END, "\nBot-> Thanks for asking me! Have a great day and I hope I helped you something!")
        elif y == 2:
            c.txt_history.insert(END, "\nBot-> It was great talking to you! Good luck coding!")
        else:
            c.txt_history.insert(END, "\nBot-> You can do it champ!")
    elif 'hey' in x:
        y = random.randint(0,2)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> Hi! Is there anything I can help you with?")
        elif y==1:
            c.txt_history.insert(END, "\nBot-> Hello! What seems to be the problem?")
        elif y==2:
            c.txt_history.insert(END, "\nBot-> Sup 😎 What can I help you with?")
    elif 'hello' in x:
        y = random.randint(0,2)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> Hi! Is there anything I can help you with?")
        elif y==1:
            c.txt_history.insert(END, "\nBot-> Hello! What seems to be the problem?")
        elif y==2:
            c.txt_history.insert(END, "\nBot-> Sup 😎 What can I help you with?")
    elif 'yo' in x:
        y = random.randint(0,2)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> Hi! Is there anything I can help you with?")
        elif y==1:
            c.txt_history.insert(END, "\nBot-> Hello! What seems to be the problem?")
        elif y==2:
            c.txt_history.insert(END, "\nBot-> Sup 😎 What can I help you with?")
    elif 'sup' in x:
        y = random.randint(0,2)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> Hi! Is there anything I can help you with?")
        elif y==1:
            c.txt_history.insert(END, "\nBot-> Hello! What seems to be the problem?")
        elif y==2:
            c.txt_history.insert(END, "\nBot-> Sup 😎 What can I help you with?")
    elif 'hi' in x:
        y = random.randint(0,2)
        if y == 0:
            c.txt_history.insert(END, "\nBot-> Hi! Is there anything I can help you with?")
        elif y==1:
            c.txt_history.insert(END, "\nBot-> Hello! What seems to be the problem?")
        elif y==2:
            c.txt_history.insert(END, "\nBot-> Sup 😎 What can I help you with?")
    else:
        c.txt_history.insert(END, "\nBot-> Please ask the question again in a different way or ask something else.")