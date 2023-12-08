import tkinter
from tkinter import messagebox
import sqlite3
import json

def cahage_password():
    win_chnp = tkinter.Toplevel()
    win_chnp.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\chnpass .png')
    label_bg = tkinter.Label(win_chnp, image=photo)
    label_bg.image = photo
    label_bg.pack()
    cnt = sqlite3.connect("register_data")
    
    # -------------------------------------------------------  username
    ety = tkinter.Entry(win_chnp, font=("LucidaSansUnicode",
                        12), bg='white', relief="flat", width=25)
    ety.place(x=750, y=258)
    # ------------------------------------------------------- oldpassword
    ety2 = tkinter.Entry(win_chnp, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=750, y=343)
    # ------------------------------------------------------- new password
    ety3 = tkinter.Entry(win_chnp, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety3.place(x=750, y=429)
    # ------------------------------------------------------- re-enter password
    ety4 = tkinter.Entry(win_chnp, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety4.place(x=750, y=513)
    # -------------------------------------------------------------------------------reecord button
    def check_oldpassword(oldpassword, username):
        cursor = cnt.cursor()
        sql = "SELECT * FROM register WHERE username=?  "
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        result_oldpass = row[2]
        if oldpassword != result_oldpass:
            messagebox.showwarning("Password Error", "old password is wrong")
            win_chnp.destroy()

    def check_newpassword(newpassword, retry_pass, oldpassword, username):
        if newpassword != retry_pass:
            messagebox.showwarning(
                "Password Error", "new password and config password not eqal")
            win_chnp.destroy()
        if oldpassword == newpassword:
            messagebox.showwarning(
                "Password Error", "old password and new password is eqal")
            win_chnp.destroy()
        else:
            update = '''UPDATE register SET password=? where username=?
            '''
            cnt.execute(update, (newpassword, username))
            cnt.commit()
            messagebox.showwarning("showwarning", "Password update")

    def updatePass():
        username = ety.get()
        
        with open("login_user.json") as f:
            user = json.load(f)
            if len(user) == 0 or user != username:
              messagebox.showwarning(
                "login Error", "login first")
              win_chnp.destroy()
              
        username = ety.get()
        
        oldpassword = ety2.get()
        check_oldpassword(oldpassword, username)
        newpassword = ety3.get()
        rery_pass = ety4.get()
        check_newpassword(newpassword, rery_pass, oldpassword,username)

    record_lbl = tkinter.Label(win_chnp, text="Record", bg="white", font=(
        "BookmanOldStyle", 15, "bold"), width=5, height=0)
    record_lbl.place(x=410, y=533)
    record_lbl.bind("<Button-1>", lambda even: updatePass())
    # --------------------------------------------------------------------------------exit

    def exit():
        win_chnp.destroy()

    exit_lbl = tkinter.Label(win_chnp, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_chnp.overrideredirect(True)
    win_chnp.mainloop()
