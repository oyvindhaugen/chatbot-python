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


def dark_mode():
    txt_history.config(bg="black", foreground="#d3d3d3")
    menu_edit.entryconfig(1, label="Light Mode", command=light_mode)
    ent_message.config(bg="black", foreground="#d3d3d3")
    btn_send.config(bg="black", foreground="#d3d3d3")
def light_mode():
    txt_history.config(bg="#d3d3d3", foreground="black")
    menu_edit.entryconfig(1, label="Dark Mode", command=dark_mode)
    ent_message.config(bg="#d3d3d3", foreground="black")
    btn_send.config(bg="#d3d3d3", foreground="black")
def send():
    txt_history.configure(state=NORMAL)
    txt_history.insert(END, "\n" + test)
    txt_history.configure(state=DISABLED)
def clear():
    txt_history.configure(state=NORMAL)
    txt_history.delete("1.0", END)
    txt_history.configure(state=NORMAL)

menu_main.add_cascade(label="File", menu=menu_file)
menu_main.add_cascade(label="Edit", menu=menu_edit)
menu_file.add_command(label="Exit", command=window.destroy)
menu_edit.add_command(label="Dark Mode", command=dark_mode)
menu_edit.add_command(label="Clear History", command=clear)
window.config(menu=menu_main)

txt_history = Text(window, bg="#d3d3d3", font=("Bahnschrift", 12), foreground="black")
txt_history.place(x=6, y=6, height=500, width=489)
test = "Bot-> Hi, my name is Bot! What is yours?"
txt_history.insert(END, test)
txt_history.configure(state=DISABLED)

ent_message = Entry(window, width=100, bg="#d3d3d3", font=("Bahnschrift", 12), foreground="black")
ent_message.place(x=6, y=510, height=67, width=420)

btn_send = Button(window, text="Send",  bg="#d3d3d3", font=("Bahnschrift", 18), activebackground="#949494", foreground="black", command=send)
btn_send.place(x=430, y=510, width=64, height=66)
window.mainloop()