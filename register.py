import tkinter
import sqlite3
from tkinter import messagebox
import login


def submit():

    win_submit = tkinter.Toplevel()
    win_submit.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\submit .png')
    label_bg = tkinter.Label(win_submit, image=photo)
    label_bg.image = photo
    label_bg.pack()
    cnt = sqlite3.connect("register_data")
    # creat_table='''CREATE TABLE register(
    #  id INTEGER PRIMARY KEY,
    #  username VARCHAR(30) NOT NULL,
    #  password VARCHAR(30) NOT NULL,
    #  email VARCHAR(100) NOT NULL)'''
    # cnt.execute(creat_table)

    # ------------------------------------------------------- username
    ety = tkinter.Entry(win_submit, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety.place(x=730, y=195)

    # ------------------------------------------------------- password
    ety2 = tkinter.Entry(win_submit, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=730, y=277)
    # ------------------------------------------------------- configpass
    ety3 = tkinter.Entry(win_submit, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety3.place(x=730, y=360)
    # #------------------------------------------------------- password
    ety4 = tkinter.Entry(win_submit, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety4.place(x=730, y=442)

    # -------------------------------------------------------------------------------register button
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
            if row is not None:
                messagebox.showwarning(
                    "Username Error", "The username already exists")
                win_submit.destroy()

    def check_password(password, rePass):
        if len(password) < 8 and password[0].islower():
            messagebox.showwarning(
                "Password Error", "password len is less than 8 or first character isn't capital,try again")
            win_submit.destroy()
        if password != rePass:
            messagebox.showwarning(
                "Password Error", "password and config password isn't match,try again")
            win_submit.destroy()

    def check_email(email):
        if "@" not in email or ".com" not in email:
            messagebox.showwarning("Email Error", "Email format is wrong")
            win_submit.destroy()
            return True
        return False

    def addData():
        username = ety.get()
        check_username(username)
        password = ety2.get()
        rePass = ety3.get()
        check_password(password, rePass)
        email = ety4.get()
        Result = check_email(email)

        if Result == False:
            add = '''INSERT INTO register(username,password,email)
            VALUES(?,?,?) 
            '''
            cnt.execute(add, (username, password, email))
            cnt.commit()
            messagebox.showwarning("", "submit successfully")

    forget_lbl = tkinter.Label(win_submit, text="Submit", bg="white", font=(
        "BookmanOldStyle", 15, "bold",), width=6, height=0)
    forget_lbl.place(x=835, y=550)
    forget_lbl.bind("<Button-1>", lambda even: addData())

    # --------------------------------------------------------------- have accunt
    def logindow():
        login.log_in()
        # win_submit.destroy()
    forget_lbl = tkinter.Label(win_submit, text="already member? login", bg="white", font=(
        "BookmanOldStyle", 7, "bold"), width=18, height=1)
    forget_lbl.place(x=704, y=486)
    forget_lbl.bind("<Button-1>", lambda even: logindow())

    # --------------------------------------------------------------------------------exit
    def exit():
        win_submit.destroy()

    exit_lbl = tkinter.Label(win_submit, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_submit.overrideredirect(True)
    win_submit.mainloop()
