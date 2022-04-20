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

#menu
menu_main = Menu(window)
#edit menu
menu_edit = Menu(window)
menu_file = Menu(window)

menu_main.add_cascade(label="File", menu=menu_file)
menu_main.add_cascade(label="edit", menu=menu_edit)
menu_file.add_command(label="Exit", command=window.destroy)
#menu_edit.add_command(label="Dark Mode", command=#add dark mode function)
#menu_edit.add_command(label="Clear History", command=#add clear function)
window.config(menu=menu_main)

window.mainloop()