from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

login_page = Tk()
login_page.title('eBook Reader - Login')
login_page.geometry('800x600')
login_page.config(bg='#F44336')


def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[2]
            pwd = row[6]

    except Exception as ep:
        messagebox.showerror('', ep)

    uname = login_name.get()
    upwd = login_password.get()
    check_counter = 0
    if uname == "":
        warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if uname == username and upwd == pwd:
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            success_login()

        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)


def success_login():
    login_page.destroy()
    import mainpage
    mainpage.main_page.mainloop()


def go_register():
    login_page.destroy()
    import registration
    registration.registration_page.mainloop()


# widgets
login_label = Label(login_page, text="Login", bg='#F44336')
login_label.config(font=("Arial", 20))

description_label = Label(login_page, text="Enter Login Details", bg='#F44336')
description_label.config(font=("Arial", 18))

login_frame = Frame(login_page, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

Label(login_frame, text="Enter Email", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=N, pady=10)

Label(login_frame, text="Enter Password", bg='#CCCCCC', font=f).grid(row=1, column=0, pady=10)

login_name = Entry(login_frame, font=f)
login_password = Entry(login_frame, font=f, show='*')
login_btn = Button(login_frame, width=15, text='Login', cursor='hand2', command=login_response)

register_btn = Button(login_frame, width=15, text='Register Now', cursor='hand2', command=go_register)

# widgets placement
login_name.grid(row=0, column=1, pady=10, padx=20)
login_password.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
register_btn.grid(row=2, column=0, pady=10, padx=20)

login_label.place(x=375, y=95)
description_label.place(x=325, y=135)
login_frame.place(x=191, y=180)

# infinite loop
login_page.mainloop()
