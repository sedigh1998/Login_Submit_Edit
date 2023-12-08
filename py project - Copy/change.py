import tkinter
import change_user
import change_pass
import change_email


def edit():
    win_edit = tkinter.Toplevel()
    win_edit.geometry("1333x750+5+0")
    photo = tkinter.PhotoImage(file='pic\edit (2).png')
    label_bg = tkinter.Label(win_edit, image=photo)
    label_bg.image = photo
    label_bg.pack()
    # --------------------------------------------------------------------------------username

    def userwin_editdow():
        change_user.changeUser()
    user_lbl = tkinter.Label(win_edit, text="Username", bg="white", font=(
        "MyriadArabic", 22, "bold"), width=8, height=0)
    user_lbl.place(x=202, y=428)
    user_lbl.bind("<Button-1>", lambda even: userwin_editdow())
    # --------------------------------------------------------------------------------password

    def passwin_editdow():
        change_pass.cahage_password()
    pass_lbl = tkinter.Label(win_edit, text="Password", bg="white", font=(
        "MyriadArabic", 21, "bold"), width=8, height=0)
    pass_lbl.place(x=597, y=428)
    pass_lbl.bind("<Button-1>", lambda even: passwin_editdow())
    # --------------------------------------------------------------------------------email

    def editwin_editdow():
        change_email.emailChange()
    edit_lbl = tkinter.Label(win_edit, text="Email", bg="white", font=(
        "MyriadArabic", 21, "bold"), width=6, height=0)
    edit_lbl.place(x=1005, y=428)
    edit_lbl.bind("<Button-1>", lambda even: editwin_editdow())

    # --------------------------------------------------------------------------------exit

    def exit():
        win_edit.destroy()

    exit_lbl = tkinter.Label(win_edit, text="Exit", font=(
        "BookmanOldStyle", 13, "bold"), bg="red")
    exit_lbl.place(x=1264, y=22)
    exit_lbl.bind("<Button-1>", lambda e: exit())

    win_edit.overrideredirect(True)
    win_edit.mainloop()
