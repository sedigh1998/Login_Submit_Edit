import tkinter
import sqlite3
import register
import change
from tkinter import messagebox
import json


def log_in():
    win_login = tkinter.Toplevel()
    win_login.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\log in page.png')
    label_bg = tkinter.Label(win_login, image=photo)
    label_bg.image = photo
    label_bg.pack()

    cnt = sqlite3.connect("register_data")
# ------------------------------------------------------- username
    ety = tkinter.Entry(win_login, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety.place(x=730, y=210)
# ------------------------------------------------------- password
    ety2 = tkinter.Entry(win_login, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=730, y=317)
# --------------------------------------------------------------------------------forget password

    def passwin():
        change.edit()
    forget_lbl = tkinter.Label(win_login, text="forget password", bg="white", font=(
        "BookmanOldStyle", 7, "bold"), width=12, height=1)
    forget_lbl.place(x=698, y=397)
    forget_lbl.bind("<Button-1>", lambda even: passwin())
# --------------------------------------------------------------- Don't have an accunt? Register now

    def registerwin():
        register.submit()
    forget_lbl = tkinter.Label(win_login, text="Don't have an accunt? Register now", bg="white", font=(
        "BookmanOldStyle", 7, "bold"), width=28, height=1)
    forget_lbl.place(x=698, y=372)
    forget_lbl.bind("<Button-1>", lambda even: registerwin())

# -------------------------------------------------------------------------------login button

    def check_username(username):
        if len(username) < 3:
            messagebox.showwarning(
                "Username Error", "Username must be at least 3 characters long")
            win_submit.destroy()
        else:
            cursor = cnt.cursor()
            sql = "SELECT * FROM register WHERE username=?"
            cursor.execute(sql, (username,))
            row = cursor.fetchone()
            if row is  None:
                messagebox.showwarning(
                    "Username Error", "please register first")
                win_submit.destroy()

         

    def check_password(password):
        if len(password) < 8 or password[0].islower():
            messagebox.showwarning(
                "Password Error", "password must be at least 8 characters long and contain at least one digit and one uppercase letter")
            win_submit.destroy()
       
    def LogInDef():
        username = ety.get()
        check_username(username)
        password = ety2.get()
        check_password(password)
            
        with open("login_user.json", "w") as f:
                json.dump(username, f)
                messagebox.showwarning("", "Wellcom to programm")

    forget_lbl = tkinter.Label(win_login, text="login", bg="white", font=(
        "BookmanOldStyle", 17, "bold"), width=4, height=0)
    forget_lbl.place(x=830, y=457)
    forget_lbl.bind("<Button-1>", lambda even: LogInDef())


# --------------------------------------------------------------------------------exit

    def exit():
        win_login.destroy()

    exit_lbl = tkinter.Label(win_login, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_login.overrideredirect(True)
    win_login.mainloop()
