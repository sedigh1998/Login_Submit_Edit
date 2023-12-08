import tkinter
from tkinter import messagebox
import json
import sqlite3


def emailChange():
    win_chnE = tkinter.Toplevel()
    win_chnE.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\chnemail.png')
    label_bg = tkinter.Label(win_chnE, image=photo)
    label_bg.image = photo
    label_bg.pack()
    cnt = sqlite3.connect("register_data")

    # -------------------------------------------------------  username
    ety = tkinter.Entry(win_chnE, font=("LucidaSansUnicode",
                        12), bg='white', relief="flat", width=25)
    ety.place(x=750, y=258)
    # ------------------------------------------------------- password
    ety2 = tkinter.Entry(win_chnE, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=750, y=343)
    # ------------------------------------------------------- email
    ety3 = tkinter.Entry(win_chnE, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety3.place(x=750, y=429)

    # -------------------------------------------------------------------------------reecord button
    def login_user(username, password):
        check = "SELECT * FROM register WHERE username=?"
        cursor = cnt.cursor()
        cursor.execute(check, (username,))
        row = cursor.fetchone()
        pas = row[2]
        if password != pas:
            messagebox.showwarning("Password error", "Password is wrong")
            win_chnE.destroy()

    def check_email(newEmail):
        if "@" not in newEmail or ".com" not in newEmail:
            messagebox.showwarning("Email Error", "Email format is wrong")
            win_chnE.destroy()

    def updateEmail():

        username = ety.get()
        with open("login_user.json") as f:
            user = json.load(f)
        if len(user) == 0:
            messagebox.showwarning("login Error", "please login first")
            win_chnE.destroy()
        elif user != username:
            messagebox.showwarning(
                "login Error", "you're not login for change password ,login first")
            win_chnE.destroy()
        password = ety2.get()
        login_user(username, password)

        newEmail = ety3.get()
        check_email(newEmail)

        update = '''UPDATE register SET email=? where username=?
            '''
        cnt.execute(update, (newEmail, username))
        cnt.commit()
        messagebox.showwarning("showwarning", "Email update")

    record_lbl = tkinter.Label(win_chnE, text="Record", bg="white", font=(
        "BookmanOldStyle", 15, "bold"), width=5, height=0)
    record_lbl.place(x=400, y=455)
    record_lbl.bind("<Button-1>", lambda even: updateEmail())
    # --------------------------------------------------------------------------------exit

    def exit():
        win_chnE.destroy()

    exit_lbl = tkinter.Label(win_chnE, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_chnE.overrideredirect(True)
    win_chnE.mainloop()
