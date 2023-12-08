import tkinter
import login
import register
import delete
import change
import json
from tkinter import messagebox

win_start = tkinter.Tk()
win_start.geometry("1333x750+5+0")
photo = tkinter.PhotoImage(file='pic\startup.png')
label_bg = tkinter.Label(win_start, image=photo)
label_bg.image = photo
label_bg.pack()
# --------------------------------------------------------------------------------login


def logwin_startdow():
    login.log_in()


login_lbl = tkinter.Label(win_start, text="Login", bg="white", font=(
    "MyriadArabic", 21, "bold"), width=4, height=0)
login_lbl.place(x=260, y=527)
login_lbl.bind("<Button-1>", lambda even: logwin_startdow())
# --------------------------------------------------------------------------------submit


def submitwin_startdow():
    register.submit()


submit_lbl = tkinter.Label(win_start, text="Submit", bg="white", font=(
    "MyriadArabic", 21, "bold"), width=6, height=0)
submit_lbl.place(x=438, y=530)
submit_lbl.bind("<Button-1>", lambda even: submitwin_startdow())
# --------------------------------------------------------------------------------edit


def editwin_startdow():
    change.edit()


edit_lbl = tkinter.Label(win_start, text="Edit", bg="white", font=(
    "MyriadArabic", 21, "bold"), width=6, height=0)
edit_lbl.place(x=635, y=530)
edit_lbl.bind("<Button-1>", lambda even: editwin_startdow())
# #--------------------------------------------------------------------------------delete


def deletewin_startdow():
    delete.Del()


del_lbl = tkinter.Label(win_start, text="Delete", bg="white", font=(
    "MyriadArabic", 21, "bold"), width=6, height=0)
del_lbl.place(x=833, y=530)
del_lbl.bind("<Button-1>", lambda even: deletewin_startdow())
# --------------------------------------------------------------------------------log out


def logout():
    with open("login_user.json", "w") as f:
        json.dump({}, f)
        messagebox.showwarning("", "logout sucssesfuly")


del_lbl = tkinter.Label(win_start, text="Logout", bg="white", font=(
    "MyriadArabic", 21, "bold"), width=6, height=0)
del_lbl.place(x=1032, y=530)
del_lbl.bind("<Button-1>", lambda even: logout())
# --------------------------------------------------------------------------------exit


def exit():
    with open("login_user.json", "w") as f:
        json.dump({}, f)
        messagebox.showwarning("", "logout sucssesfuly")
    win_start.destroy()


exit_lbl = tkinter.Label(win_start, text="Exit", font=(
    "BookmanOldStyle", 13, "bold"), bg="red")
exit_lbl.place(x=1264, y=22)
exit_lbl.bind("<Button-1>", lambda e: exit())

win_start.overrideredirect(True)
win_start.mainloop()
