from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text,
                    password text
                )
            ''')
con.commit()

            

ws = Tk()
ws.title('Login')
ws.geometry('940x500')
ws.config(bg='#0B5A81')


def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[2]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)



# widgets
left_frame = Frame( 
    ws,
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=N, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    )


# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)


# infinite loop
ws.mainloop()
