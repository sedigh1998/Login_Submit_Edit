import tkinter
import sqlite3
from tkinter import messagebox
import login


def Del():
    win_del = tkinter.Toplevel()
    win_del.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\delete.png')
    label_bg = tkinter.Label(win_del, image=photo)
    label_bg.image = photo
    label_bg.pack()
    cnt = sqlite3.connect("register_data")
# ------------------------------------------------------- username
    ety = tkinter.Entry(win_del, font=("LucidaSansUnicode", 12),
                        bg='white', relief="flat", width=25)
    ety.place(x=730, y=210)
# ------------------------------------------------------- password
    ety2 = tkinter.Entry(win_del, font=(
        "LucidaSansUnicode", 12), bg='white', relief="flat", width=25)
    ety2.place(x=730, y=317)
#------------------------------------------------------------------------
    def check_username(username):
        if len(username) < 3:
            messagebox.showwarning(
                "Username Error", "Username must be at least 3 characters long")
            win_submit.destroy()
        
         

    def check_password(password):
        if len(password) < 8 or password[0].islower():
            messagebox.showwarning(
                "showwarning", "password must be at least 8 characters long and contain at least one digit and one uppercase letter")
            win_submit.destroy()

# -------------------------------------------------------------------------------del button


    def delete_user():
        username = ety.get()
        check_username(username)
        password = ety2.get()
        check_password(password)

        delete = '''DELETE FROM register  WHERE username =?'''
        result = cnt.execute(delete, (username,))

        cnt.commit()
        messagebox.showwarning("Delete", "user delete")
    forget_lbl = tkinter.Label(win_del, text="Delete", bg="white", font=(
        "BookmanOldStyle", 15, "bold"), width=5, height=0)
    forget_lbl.place(x=827, y=457)
    forget_lbl.bind("<Button-1>", lambda even: delete_user())


# --------------------------------------------------------------------------------exit

    def exit():
        win_del.destroy()

    exit_lbl = tkinter.Label(win_del, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_del.overrideredirect(True)
    win_del.mainloop()
