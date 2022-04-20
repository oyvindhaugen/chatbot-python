from tkinter import *

#These are the basic settings for my window
window = Tk()
window.geometry("500x600")
#window size
window.title("Chatbot")
#title
window.resizable(width=FALSE, height=FALSE)

#window icon
icon = PhotoImage(file ="icon_bot.png")
window.iconphoto(False, icon)



window.mainloop()