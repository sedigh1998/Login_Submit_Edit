import tkinter
from tkinter import messagebox
import json
import sqlite3


def changeUser():

    win_chnu = tkinter.Toplevel()
    win_chnu.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\chnUser .png')
    label_bg = tkinter.Label(win_chnu, image=photo)
    label_bg.image = photo
    label_bg.pack()
    cnt = sqlite3.connect("register_data")
    # ------------------------------------------------------- old username
    ety = tkinter.Entry(win_chnu, font=("LucidaSansUnicode",
                        12), bg='white', relief="flat", width=25)
    ety.place(x=730, y=215)
    # ------------------------------------------------------- new username
    ety2 = tkinter.Entry(win_chnu, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=730, y=318)
    # ------------------------------------------------------- password
    ety3 = tkinter.Entry(win_chnu, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety3.place(x=730, y=420)

    # -------------------------------------------------------------------------------reecord button

    def check_oldusername(old_username):
        with open("login_user.json")as f:
            loginUser = json.load(f)
        if loginUser != old_username:
            messagebox.showwarning("", "first login")
            win_chnu.destroy()
            
        elif len(old_username) < 3:
            messagebox.showwarning(
                "Username Error", "Username must be at least 3 characters long")
            win_chnu.destroy()
        
                
    def check_newusername(new_username):
        if len(new_username) < 3:
            messagebox.showwarning(
                "Username Error", "Username must be at least 3 characters long")
            win_chnu.destroy()
        else:
            cursor = cnt.cursor()
            sql = "SELECT * FROM register WHERE username=?"
            cursor.execute(sql, (new_username,))
            row = cursor.fetchone()
            if row is not None:
                messagebox.showwarning(
                    "Username Error", "The username already exists")
                win_chnu.destroy()

    def check_password(password,new_username, old_username):
        if len(password) < 8 or password[0].islower():
            messagebox.showwarning(
                "showwarning", "password must be at least 8 characters long and contain at least one digit and one uppercase letter")
            win_chnu.destroy()
        else:
            update = '''UPDATE register SET username=? where username=?
            '''
            cnt.execute(update, (new_username, old_username))
            cnt.commit()
            messagebox.showwarning("showwarning", "Username update")
            
            with open("login_user.json")as f:
             json.dump(new_username,f)
            
    def cahngeDef():
        old_username = ety.get()
        check_oldusername(old_username)

        new_username = ety2.get()
        check_newusername(new_username)

        password = ety3.get()
        check_password(password,new_username,old_username)

        

    record_lbl = tkinter.Label(win_chnu, text="Record", bg="white", font=(
        "BookmanOldStyle", 15, "bold"), width=5, height=0)
    record_lbl.place(x=820, y=515)
    record_lbl.bind("<Button-1>", lambda even: cahngeDef())
    # --------------------------------------------------------------------------------exit

    def exit():
        win_chnu.destroy()

    exit_lbl = tkinter.Label(win_chnu, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_chnu.overrideredirect(True)
    win_chnu.mainloop()
