import os
import shutil
import sqlite3
import tkinter as tk
from tkinter import SOLID, N, messagebox, W, LEFT, RIDGE, BOTH, RIGHT, TOP, filedialog, END, ttk
from PIL import Image, ImageTk
from pdf2image import convert_from_path
from chatclient import Client
from db_handle import *

f = ('Arial', 14)
HOST = '127.0.0.1'
PORT = 8080
pop_path = "/usr/local/Cellar/poppler/21.11.0/bin"  # need this to work on mac for some reason


def resetMainPage():
    randomLists()
    newBook1 = Image.open(coverList[0])
    newBook1 = newBook1.resize((131, 170), Image.ANTIALIAS)
    Book1 = ImageTk.PhotoImage(newBook1)
    book1_label.configure(image=Book1)
    book1_label.image = Book1

    newBook2 = Image.open(coverList[1])
    newBook2 = newBook2.resize((131, 170), Image.ANTIALIAS)
    Book2 = ImageTk.PhotoImage(newBook2)
    book2_label.configure(image=Book2)
    book2_label.image = Book2

    newBook3 = Image.open(coverList[2])
    newBook3 = newBook3.resize((131, 170), Image.ANTIALIAS)
    Book3 = ImageTk.PhotoImage(newBook3)
    book3_label.configure(image=Book3)
    book3_label.image = Book3

    newBook4 = Image.open(coverList[3])
    newBook4 = newBook4.resize((131, 170), Image.ANTIALIAS)
    Book4 = ImageTk.PhotoImage(newBook4)
    book4_label.configure(image=Book4)
    book4_label.image = Book4

    newBook5 = Image.open(coverList[4])
    newBook5 = newBook5.resize((131, 170), Image.ANTIALIAS)
    Book5 = ImageTk.PhotoImage(newBook5)
    book5_label.configure(image=Book5)
    book5_label.image = Book5

    newBook6 = Image.open(coverList[5])
    newBook6 = newBook6.resize((131, 170), Image.ANTIALIAS)
    Book6 = ImageTk.PhotoImage(newBook6)
    book6_label.configure(image=Book6)
    book6_label.image = Book6


def resetSearchPage():
    if len(idList) > 0:
        newBook1S = Image.open(coverList[0])
        newBook1S = newBook1S.resize((131, 170), Image.ANTIALIAS)
        newBook1S = ImageTk.PhotoImage(newBook1S)
        book1S_label.configure(image=newBook1S)
        book1S_label.image = newBook1S
        book1S_label.place(x=225, y=160)
        book1S_btn.place(x=225, y=345)
    else:
        book1S_label.pack_forget()

    if len(idList) > 1:
        book2S_label.pack()
        newBook2S = Image.open(coverList[1])
        newBook2S = newBook2S.resize((131, 170), Image.ANTIALIAS)
        newBook2S = ImageTk.PhotoImage(newBook2S)
        book2S_label.configure(image=newBook2S)
        book2S_label.image = newBook2S
        book2S_label.place(x=400, y=160)
        book2S_btn.place(x=400, y=345)
    else:
        book2S_label.pack_forget()

    if len(idList) > 2:
        newBook3S = Image.open(coverList[0])
        newBook3S = newBook3S.resize((131, 170), Image.ANTIALIAS)
        newBook3S = ImageTk.PhotoImage(newBook3S)
        book3S_label.configure(image=newBook3S)
        book3S_label.image = newBook3S
        book3S_label.place(x=575, y=160)
        book3S_btn.place(x=575, y=345)

    if len(idList) > 3:
        newBook4S = Image.open(coverList[3])
        newBook4S = newBook4S.resize((131, 170), Image.ANTIALIAS)
        newBook4S = ImageTk.PhotoImage(newBook4S)
        newBook4S_label.image = newBook4S
        newBook4S_label.place(x=225, y=390)
        newBook4S_btn.place(x=225, y=575)

    if len(idList) > 4:
        newBook5S = Image.open(coverList[4])
        newBook5S = newBook5S.resize((131, 170), Image.ANTIALIAS)
        newBook5S = ImageTk.PhotoImage(newBook5S)
        newBook5S_label = tk.Label(self, image=newBook5S)
        newBook5S_label.image = newBook5S
        newBook5S_label.place(x=400, y=390)
        newBook5S_btn.place(x=400, y=575)

    if len(idList) > 5:
        newBook6S = Image.open(coverList[5])
        newBook6S = newBook6S.resize((131, 170), Image.ANTIALIAS)
        newBook6S = ImageTk.PhotoImage(newBook6S)
        newBook6S_label = tk.Label(self, image=newBook6S)
        newBook6S_label.image = newBook6S
        newBook6S_label.place(x=575, y=390)
        newBook6S_btn.place(x=575, y=575)


def resetDetailsPage(x):
    newBookD = Image.open(coverList[x])
    newBookD = newBookD.resize((131, 170), Image.ANTIALIAS)
    BookD = ImageTk.PhotoImage(newBookD)
    bookD_label.configure(image=BookD)
    bookD_label.image = BookD
    author_label.configure(text=authorList[x])
    title_label.configure(text=titleList[x])
    synopsis_label.configure(text=synopsisList[x])


def resetReader(x):
    pages = convert_from_path(pathList[x], size=(800, 900), poppler_path=pop_path)

    newPhotos = []

    for i in range(len(pages)):
        newPhotos.append(ImageTk.PhotoImage(pages[i]))

    pdf.delete('1.0', tk.END)

    for photo in newPhotos:
        pdf.image_create(tk.END, image=photo)

        pdf.insert(tk.END, '\n\n')

        pdf.newPhotos = newPhotos


def resetProfile():
    global login_details
    login_details.clear()
    login_details = list(logged_in_user(user[0]))


def logged_in_user(username):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from record WHERE email= ?"
    cursor.execute(query, (username,))
    userRecord = cursor.fetchone()
    return userRecord


user = ['test@test.com']

login_details = list(logged_in_user(user[0]))


def searchMain():
    searchQuery = search_entry.get()
    search(searchQuery)


def searchSide():
    searchQuery = search_entry_side.get()
    search(searchQuery)


def hideWidget(event):
    event.pack_forget()


def clearSearchWidget():
    hideWidget(book1S_label)
    hideWidget(book2S_label)
    hideWidget(book3S_label)
    hideWidget(book4S_label)
    hideWidget(book5S_label)
    hideWidget(book6S_label)
    hideWidget(book1S_btn)
    hideWidget(book2S_btn)
    hideWidget(book3S_btn)
    hideWidget(book4S_btn)
    hideWidget(book5S_btn)
    hideWidget(book6S_btn)


login_details = list(logged_in_user(user[0]))


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                StartPage, LoginPage, RegistrationPage, MainPage, ProfilePage, UploadPage, DetailPage, MyLibrary,
                ReaderPage, SearchPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def refreshMain(self, cont):
        resetMainPage()
        frame = self.frames[cont]
        frame.tkraise()

    def refreshDetail(self, cont, x):
        resetDetailsPage(x)
        setCurrentBook(x)
        frame = self.frames[cont]
        frame.tkraise()

    def refreshReader(self, cont, x):
        resetReader(x)
        frame = self.frames[cont]
        frame.tkraise()

    def refreshMainSearch(self, cont):
        searchMain()
        clearSearchWidget()
        resetSearchPage()
        frame = self.frames[cont]
        frame.tkraise()

    def refreshSideSearch(self, cont):
        searchSide()
        clearSearchWidget()
        resetSearchPage()

    def refreshProfile(self, cont):
        resetProfile()
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#95A7A7')

        book_logo = Image.open('../ALL Project 1/book.png')
        book_logo = book_logo.resize((400, 300), Image.ANTIALIAS)
        book_logo = ImageTk.PhotoImage(book_logo)
        logo_canvas = tk.Canvas(self, bg='#CABFBF', width=500, height=450)
        logo_canvas.image = book_logo
        logo_canvas.create_image(250, 220, image=book_logo)
        logo_canvas.place(x=145, y=70)

        label = tk.Label(self, text='Welcome to eBook Reader', bg='#CABFBF')
        label.config(font=("sans", 20, 'bold'))

        or_label = tk.Label(self, text='OR', bg='#CABFBF')
        or_label.config(font=("Verdana", 12, 'italic'))

        login_btn = tk.Button(self, width=22, height=2, text='Login',
                              command=lambda: controller.show_frame(LoginPage))
        register_btn = tk.Button(self, width=22, height=2, text='Register',
                                 command=lambda: controller.show_frame(RegistrationPage))

        label.place(x=270, y=95)
        or_label.place(x=384, y=477)
        login_btn.place(x=175, y=470)
        register_btn.place(x=420, y=470)


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')

        login_label = tk.Label(self, text="Login Page", bg='#BFCACA')
        login_label.config(font=("Verdana", 20, 'bold'))

        description_label = tk.Label(self, text="Enter Login Details", bg='#BFCACA')
        description_label.config(font=("Verdana", 18, 'italic'))

        login_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

        tk.Label(login_frame, text="Enter Email", bg='#CCCCCC').grid(row=0, column=0, sticky=N, pady=10)

        tk.Label(login_frame, text="Enter Password", bg='#CCCCCC').grid(row=1, column=0, pady=10)

        login_name = tk.Entry(login_frame)
        login_password = tk.Entry(login_frame, show='*')
        login_btn = tk.Button(login_frame, width=15, text='Login', cursor='hand2',
                              command=lambda: login_response())

        register_btn = tk.Button(login_frame, width=15, text='Register Now', cursor='hand2',
                                 command=lambda: controller.show_frame(RegistrationPage))

        login_name.grid(row=0, column=1, pady=10, padx=20)
        login_password.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        register_btn.grid(row=2, column=0, pady=10, padx=20)

        login_label.place(x=340, y=95)
        description_label.place(x=315, y=135)
        login_frame.place(x=191, y=180)

        def login_response():
            global login_details
            try:
                con = sqlite3.connect('userdata.db')
                c = con.cursor()
                for row in c.execute("Select * from record"):
                    username = row[2]
                    pwd = row[6]

            except Exception as ep:
                messagebox.showerror('', ep)

            email = login_name.get()
            password = login_password.get()
            check_counter = 0
            if email == "":
                warn = "Username can't be empty"
            else:
                check_counter += 1
            if password == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1
            if check_counter == 2:
                if email == username and password == pwd:
                    messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    user.insert(0, str(login_name.get()))
                    login_details = list(logged_in_user(user[0]))
                    print(login_details)
                    login_name.delete(0, 'end')
                    login_password.delete(0, 'end')
                    controller.show_frame(MainPage)

                else:
                    messagebox.showerror('Login Status', 'invalid username or password')
            else:
                messagebox.showerror('', warn)


class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS record(
                            user_id integer primary key autoincrement,
                            name text, 
                            email text, 
                            contact number, 
                            gender text, 
                            country text,
                            password text
                        )
                    ''')
        con.commit()

        tk.Frame.__init__(self, parent, bg='#BFCACA')
        var = tk.StringVar()
        var.set('male')

        countries = []
        variable = tk.StringVar()
        world = open('countries.txt', 'r')
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[106])

        # widgets
        registration_lbl = tk.Label(self, text="Registration Page", bg='#BFCACA')
        registration_lbl.config(font=("Verdana", 20, 'bold'))

        registration_desc = tk.Label(self, text="Create A New Account", bg='#BFCACA')
        registration_desc.config(font=("Verdana", 18, 'italic'))

        mainFrame = tk.Frame(self, bd=0, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

        tk.Label(mainFrame, text="Enter Name", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Enter Email", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Contact Number", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Select Gender", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Select Country", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Enter Password", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Re-Enter Password", bg='#CCCCCC', font=f).grid(row=6, column=0, sticky=W, pady=10)

        gender_frame = tk.LabelFrame(mainFrame, bg='#CCCCCC', padx=10, pady=10, )
        register_name = tk.Entry(mainFrame, font=f)
        register_email = tk.Entry(mainFrame, font=f)
        register_mobile = tk.Entry(mainFrame, font=f)

        male_rb = tk.Radiobutton(gender_frame, text='Male', bg='#CCCCCC', variable=var, value='male',
                                 font=('Times', 10))
        female_rb = tk.Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female',
                                   font=('Times', 10))

        register_country = tk.OptionMenu(mainFrame, variable, *countries)
        register_country.config(width=15, font=('Times', 12))

        register_pwd = tk.Entry(mainFrame, font=f, show='*')
        pwd_again = tk.Entry(mainFrame, font=f, show='*')

        register_btn = tk.Button(mainFrame, width=15, text='Join Now!', bg='green', font=f, relief=SOLID,
                                 cursor='hand2',
                                 command=lambda: insert_record())

        back_btn = tk.Button(mainFrame, text='Already have an account', font=f, relief=SOLID, cursor='hand2',
                             command=lambda: controller.show_frame(LoginPage))

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_country.grid(row=4, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=0, pady=10, padx=20)
        back_btn.grid(row=7, column=1, pady=10, padx=20)

        registration_lbl.place(x=310, y=30)
        registration_desc.place(x=310, y=65)
        mainFrame.place(x=215, y=110)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)

        def insert_record():
            check_counter = 0
            warn = ""
            if register_name.get() == "":
                warn = "Name can't be empty"
            else:
                check_counter += 1

            if register_email.get() == "":
                warn = "Email can't be empty"
            else:
                check_counter += 1

            if register_mobile.get() == "":
                warn = "Contact can't be empty"
            else:
                check_counter += 1

            if var.get() == "":
                warn = "Select Gender"
            else:
                check_counter += 1

            if variable.get() == "":
                warn = "Select Country"
            else:
                check_counter += 1

            if register_pwd.get() == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1

            if pwd_again.get() == "":
                warn = "Re-enter password can't be empty"
            else:
                check_counter += 1

            if register_pwd.get() != pwd_again.get():
                warn = "Passwords didn't match!"
            else:
                check_counter += 1

            if check_counter == 8:
                try:
                    con = sqlite3.connect('userdata.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO record (name, email, contact, gender, country, password) VALUES (:name, :email, "
                        ":contact, :gender, :country, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

                        })
                    con.commit()
                    messagebox.showinfo('confirmation', 'Record Saved')
                    controller.show_frame(LoginPage)

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        self.controller = controller

        categories = ['All Categories', 'Action and Adventure', 'Self Improvement', 'Mystery', 'Horror', 'Fantasy',
                      'Sci-Fi', 'Romance', 'Crime', 'History']
        mainFrame = tk.Frame(self)
        top_frame = tk.Frame(self, bg='#CCCCCC')
        sidebar_frame = tk.Frame(self, bg="#CCCCCC", borderwidth=2, relief=RIDGE)

        variable = tk.StringVar()
        variable.set(categories[0])

        book1 = Image.open(coverList[0])
        book1 = book1.resize((131, 170), Image.ANTIALIAS)
        book1 = ImageTk.PhotoImage(book1)
        global book1_label
        book1_label = tk.Label(self, image=book1)
        book1_label.image = book1
        book1_label.place(x=225, y=160)
        book1_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 0))
        book1_btn.place(x=225, y=345)

        book2 = Image.open(coverList[1])
        book2 = book2.resize((131, 170), Image.ANTIALIAS)
        book2 = ImageTk.PhotoImage(book2)
        global book2_label
        book2_label = tk.Label(self, image=book2)
        book2_label.image = book2
        book2_label.place(x=400, y=160)
        book2_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 1))
        book2_btn.place(x=400, y=345)

        book3 = Image.open(coverList[2])
        book3 = book3.resize((131, 170), Image.ANTIALIAS)
        book3 = ImageTk.PhotoImage(book3)
        global book3_label
        book3_label = tk.Label(self, image=book3)
        book3_label.image = book3
        book3_label.place(x=575, y=160)
        book3_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 2))
        book3_btn.place(x=575, y=345)

        book4 = Image.open(coverList[3])
        book4 = book4.resize((131, 170), Image.ANTIALIAS)
        book4 = ImageTk.PhotoImage(book4)
        global book4_label
        book4_label = tk.Label(self, image=book4)
        book4_label.image = book4
        book4_label.place(x=225, y=390)
        book4_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 3))
        book4_btn.place(x=225, y=575)

        book5 = Image.open(coverList[4])
        book5 = book5.resize((131, 170), Image.ANTIALIAS)
        book5 = ImageTk.PhotoImage(book5)
        global book5_label
        book5_label = tk.Label(self, image=book5)
        book5_label.image = book5
        book5_label.place(x=400, y=390)
        book5_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 4))
        book5_btn.place(x=400, y=575)

        book6 = Image.open(coverList[5])
        book6 = book6.resize((131, 170), Image.ANTIALIAS)
        book6 = ImageTk.PhotoImage(book6)
        global book6_label
        book6_label = tk.Label(self, image=book6)
        book6_label.image = book6
        book6_label.place(x=575, y=390)
        book6_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.refreshDetail(DetailPage, 5))
        book6_btn.place(x=575, y=575)

        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("sans", 20, 'bold'))

        featured_lbl = tk.Label(self, text="Featured Reads", bg='#BFCACA')
        featured_lbl.config(font=("sans", 18, 'italic'))

        main_btn = tk.Button(top_frame, text='Main Page', state='disabled')
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.refreshProfile(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        global search_entry
        search_entry = tk.Entry(mainFrame, width=67, font=f)
        search_entry.pack(side=LEFT, fill=BOTH, expand=1)
        search_entry.insert(0, "Search eBooks by title, author, or ISBN")

        category_filter = tk.OptionMenu(mainFrame, variable, *categories)
        category_filter.pack(side=LEFT)

        search_button = tk.Button(mainFrame, text='Search', command=lambda: controller.refreshMainSearch(SearchPage))
        search_button.pack(side=RIGHT)
        mainFrame.pack(side=TOP)

        recommendations_btn = tk.Button(sidebar_frame, text='Recommendations')
        categories_btn = tk.Button(sidebar_frame, text='Categories')
        chat_btn = tk.Button(sidebar_frame, text='World Chat', command=lambda: Client(HOST, PORT))
        upload_btn = tk.Button(sidebar_frame, text='Upload an eBook', command=lambda: controller.show_frame(UploadPage))

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        recommendations_btn.grid(row=0, column=0, padx=10, pady=5)
        categories_btn.grid(row=1, column=0, padx=10, pady=5)
        chat_btn.grid(row=3, column=0, padx=10, pady=5)
        upload_btn.grid(row=2, column=0, padx=10, pady=5)

        mainFrame.place(x=41, y=70)
        top_frame.place(x=426, y=20)
        sidebar_frame.place(x=40, y=120)
        header_label.place(x=40, y=20)
        featured_lbl.place(x=225, y=120)

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')


class DetailPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.refreshMain(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        bookD = Image.open(coverList[0])
        bookD = bookD.resize((131, 170), Image.ANTIALIAS)
        bookD = ImageTk.PhotoImage(bookD)
        global bookD_label
        bookD_label = tk.Label(self, image=bookD)
        bookD_label.image = bookD
        bookD_label.place(x=40, y=80)

        global title_label
        title_label = tk.Label(self, bg='#BFCACA', text=titleList[0])
        title_label.config(font=("Sans", 20, 'bold'))
        global author_label
        author_label = tk.Label(self, bg='#BFCACA', text=authorList[0])
        author_label.config(font=("Sans", 20, 'bold'))
        global synopsis_label
        synopsis_label = tk.Message(self, bg='#BFCACA', width=400, text=synopsisList[0])
        synopsis_label.config(font=("Sans", 16, 'italic'))
        title_label.place(x=200, y=80)
        author_label.place(x=200, y=110)
        synopsis_label.place(x=200, y=150)

        review_label = tk.Label(self, bg='#BFCACA', text='Ratings & Reviews')
        review_label.config(font=("Sans", 20, 'bold'))
        review_label.place(x=40, y=375)

        read_btn = tk.Button(self, width=15, text='Begin Reading',
                             command=lambda: controller.refreshReader(ReaderPage, currentBook[0]))
        add_fav = tk.Button(self, width=15, text='Add to My Library')
        download_btn = tk.Button(self, width=15, text='Download', command=lambda: download_book(0))

        reviewFrame = tk.Frame(self, bg='#BFCACA')
        ratingFrame = tk.Frame(reviewFrame)
        review_entry = tk.Entry(reviewFrame, width=55, font=f)
        review_entry.pack(side=LEFT, fill=BOTH, expand=1)

        var = tk.StringVar()
        var.set('1')

        one_rb = tk.Radiobutton(ratingFrame, text='1', bg='#CABFBF', variable=var, value='1', font=f)
        two_rb = tk.Radiobutton(ratingFrame, text='2', bg='#CABFBF', variable=var, value='2', font=f)
        three_rb = tk.Radiobutton(ratingFrame, text='3', bg='#CABFBF', variable=var, value='3', font=f)
        four_rb = tk.Radiobutton(ratingFrame, text='4', bg='#CABFBF', variable=var, value='4', font=f)
        five_rb = tk.Radiobutton(ratingFrame, text='5', bg='#CABFBF', variable=var, value='5', font=f)
        one_rb.pack(expand=True, side=LEFT)
        two_rb.pack(expand=True, side=LEFT)
        three_rb.pack(expand=True, side=LEFT)
        four_rb.pack(expand=True, side=LEFT)
        five_rb.pack(expand=True, side=LEFT)

        enter_button = tk.Button(reviewFrame, text='Enter')
        review_entry.grid(row=0, column=0, padx=10, pady=5)
        ratingFrame.grid(row=0, column=1, padx=10, pady=5)
        enter_button.grid(row=0, column=2, padx=10, pady=5)

        reviewFrame.place(x=32, y=410)

        read_btn.place(x=625, y=120)
        add_fav.place(x=625, y=160)
        download_btn.place(x=625, y=200)

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')


class ReaderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        reader_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.refreshMain(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=15)
        reader_frame.place(x=10, y=65)
        header_label.place(x=40, y=20)

        # PDF is converted to a list of images
        pages = convert_from_path(pathList[0], size=(800, 900), poppler_path=pop_path)  # needed pop_path to run

        # Empty list for storing images
        photos = []

        tab_control = ttk.Notebook(reader_frame)
        tab_control.place(x=10, y=10, height=600, width=800)
        scroll_y = tk.Scrollbar(reader_frame, orient=tk.VERTICAL)
        scroll_y.grid(row=0, column=1, sticky='ns')
        global pdf
        pdf = tk.Text(reader_frame, height=43, width=108, yscrollcommand=scroll_y.set, bg="grey")
        pdf.grid(row=0, column=0)
        scroll_y.config(command=pdf.yview)

        # Storing the converted images into list
        for i in range(len(pages)):
            photos.append(ImageTk.PhotoImage(pages[i]))

        # Clear the text box
        pdf.delete('1.0', tk.END)

        # Adding all the images to the text widget
        for photo in photos:
            pdf.image_create(tk.END, image=photo)

            # For Separating the pages
            pdf.insert(tk.END, '\n\n')

            pdf.photos = photos  # used an attribute of "pdf" to store the references

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')


class MyLibrary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.refreshMain(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', state='disabled')
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)

        book1 = Image.open(coverList[0])
        book1 = book1.resize((131, 170), Image.ANTIALIAS)
        book1 = ImageTk.PhotoImage(book1)
        book1_label = tk.Label(self, image=book1)
        book1_label.image = book1
        book1_label.place(x=225, y=160)
        book1_btn = tk.Button(self, width=15, text='View Book')
        book1_btn.place(x=225, y=345)

        book2 = Image.open(coverList[1])
        book2 = book2.resize((131, 170), Image.ANTIALIAS)
        book2 = ImageTk.PhotoImage(book2)
        book2_label = tk.Label(self, image=book2)
        book2_label.image = book2
        book2_label.place(x=400, y=160)
        book2_btn = tk.Button(self, width=15, text='View Book')
        book2_btn.place(x=400, y=345)

        book3 = Image.open(coverList[2])
        book3 = book3.resize((131, 170), Image.ANTIALIAS)
        book3 = ImageTk.PhotoImage(book3)
        book3_label = tk.Label(self, image=book3)
        book3_label.image = book3
        book3_label.place(x=575, y=160)
        book3_btn = tk.Button(self, width=15, text='View Book')
        book3_btn.place(x=575, y=345)

        book4 = Image.open(coverList[3])
        book4 = book4.resize((131, 170), Image.ANTIALIAS)
        book4 = ImageTk.PhotoImage(book4)
        book4_label = tk.Label(self, image=book4)
        book4_label.image = book4
        book4_label.place(x=225, y=390)
        book4_btn = tk.Button(self, width=15, text='View Book')
        book4_btn.place(x=225, y=575)

        book5 = Image.open(coverList[4])
        book5 = book5.resize((131, 170), Image.ANTIALIAS)
        book5 = ImageTk.PhotoImage(book5)
        book5_label = tk.Label(self, image=book5)
        book5_label.image = book5
        book5_label.place(x=400, y=390)
        book5_btn = tk.Button(self, width=15, text='View Book')
        book5_btn.place(x=400, y=575)

        book6 = Image.open(coverList[5])
        book6 = book6.resize((131, 170), Image.ANTIALIAS)
        book6 = ImageTk.PhotoImage(book6)
        book6_label = tk.Label(self, image=book6)
        book6_label.image = book6
        book6_label.place(x=575, y=390)
        book6_btn = tk.Button(self, width=15, text='View Book')
        book6_btn.place(x=575, y=575)

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        global login_details
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.refreshMain(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', state='disabled')
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        # profile pic
        pic = Image.open('profilepic.jpeg')
        pic = pic.resize((100, 100), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        pic_label = tk.Label(self, image=pic)
        pic_label.image = pic
        pic_label.place(x=40, y=80)

        # details
        name_label = tk.Label(self, text=("Welcome," + login_details[1] + "!"), bg='#BFCACA')
        name_label.config(font=('courier', 20))
        name_label.place(x=170, y=100)

        details_label = tk.Label(self, text="Profile Details", font=('Verdana', 18), bg='#BFCACA')
        details_label.place(x=40, y=200)

        edit_profile = tk.Button(self, text="Edit Profile", command=lambda: edit_profile())
        edit_profile.place(x=180, y=140)

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)

        # user details
        mainFrame = tk.Frame(self, bd=0, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

        tk.Label(mainFrame, text="Name", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Email", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Number", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Gender", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Country", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)

        gender_frame = tk.LabelFrame(mainFrame, bg='#CCCCCC', padx=10, pady=10, )
        usr_name = tk.Entry(mainFrame, font=f)
        usr_name.insert(0, login_details[1])
        usr_name.config(state='disable')
        usr_email = tk.Entry(mainFrame, font=f)
        usr_email.insert(0, login_details[2])
        usr_email.config(state='disable')
        usr_mobile = tk.Entry(mainFrame, font=f)
        usr_mobile.insert(0, login_details[3])
        usr_mobile.config(state='disable')

        var = tk.StringVar()
        var.set('male')

        countries = []
        variable = tk.StringVar()
        world = open('countries.txt', 'r')
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[106])

        male_rb = tk.Radiobutton(gender_frame, text='Male', bg='#CCCCCC', variable=var, value='male',
                                 font=('Times', 10))
        female_rb = tk.Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female',
                                   font=('Times', 10))

        usr_country = tk.OptionMenu(mainFrame, variable, *countries)
        usr_country.config(width=15, font=('Times', 12), state='disable')

        usr_name.grid(row=0, column=1, pady=10, padx=20)
        usr_email.grid(row=1, column=1, pady=10, padx=20)
        usr_mobile.grid(row=2, column=1, pady=10, padx=20)
        usr_country.grid(row=4, column=1, pady=10, padx=20)
        mainFrame.place(x=40, y=250)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)

        save_btn = tk.Button(self, text='Save Changes', command=lambda: edit_record())

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')

        def edit_profile():
            usr_name.config(state='normal')
            usr_email.config(state='normal')
            usr_mobile.config(state='normal')
            usr_country.config(state='normal')

            save_btn.pack()
            save_btn.place(x=130, y=535)

        def edit_record():
            usr_name.config(state='disable')
            usr_email.config(state='disable')
            usr_mobile.config(state='disable')
            usr_country.config(state='disable')

            save_btn.pack_forget()


class UploadPage(tk.Frame):
    def __init__(self, parent, controller):
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS books(
                            book_id integer primary key autoincrement,
                            title text, 
                            author text,
                            ISBN number, 
                            synopsis text, 
                            category text,
                            path text,
                            cover text
                        )
                    ''')
        con.commit()

        tk.Frame.__init__(self, parent, bg='#BFCACA')
        categories = ['Action and Adventure', 'Self Improvement', 'Mystery', 'Horror', 'Fantasy', 'Sci-Fi', 'Romance',
                      'Crime', 'History']
        variable = tk.StringVar()
        variable.set(categories[0])

        # widget
        upload_label = tk.Label(self, text="Upload Page", bg='#BFCACA')
        upload_label.config(font=("Verdana", 20, 'bold'))

        upload_des = tk.Label(self, text="Upload your eBooks to the eReader!", bg='#BFCACA')
        upload_des.config(font=("Verdana", 18, 'italic'))

        mainFrame = tk.Frame(self, bd=0, bg='#CCCCCC', relief=RIDGE, padx=10, pady=10)

        tk.Label(mainFrame, text="Title", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="Author", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="ISBN", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="Synopsis", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="Category", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="Upload File", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)

        tk.Label(mainFrame, text="Upload Cover", bg='#CCCCCC', font=f).grid(row=7, column=0, sticky=W, pady=10)

        book_title = tk.Entry(mainFrame, font=f, width=50)

        book_author = tk.Entry(mainFrame, font=f, width=50)

        book_ISBN = tk.Entry(mainFrame, font=f, width=50)

        book_synopsis = tk.Entry(mainFrame, font=f, width=50)

        book_category = tk.OptionMenu(mainFrame, variable, *categories)
        book_category.config(width=62, font=('Times', 12))

        book_link = tk.Entry(mainFrame, font=f, width=50)

        cover_link = tk.Entry(mainFrame, font=f, width=50)

        choose_btn = tk.Button(mainFrame, width=50, text='Choose a file to upload', font=f, relief=SOLID,
                               cursor='hand2', command=lambda: choose_file())

        cover_btn = tk.Button(mainFrame, width=50, text='Choose a file to upload', font=f, relief=SOLID,
                              cursor='hand2', command=lambda: choose_cover())

        upload_btn = tk.Button(mainFrame, width=50, text='Upload book!', bg='green', font=f, relief=SOLID,
                               cursor='hand2', command=lambda: insert_book())

        back_btn = tk.Button(mainFrame, text='Back to main page', font=f, relief=SOLID, cursor='hand2',
                             command=lambda: controller.show_frame(MainPage))

        book_title.grid(row=0, column=1, pady=10, padx=20)
        book_author.grid(row=1, column=1, pady=10, padx=20)
        book_ISBN.grid(row=2, column=1, pady=10, padx=20)
        book_synopsis.grid(row=3, column=1, pady=10, padx=20)
        book_category.grid(row=4, column=1, pady=10, padx=20)
        book_link.grid(row=5, column=1, pady=10, padx=20)
        cover_link.grid(row=7, column=1, pady=10, padx=20)

        choose_btn.grid(row=6, column=1, pady=10, padx=20)
        cover_btn.grid(row=8, column=1, pady=10, padx=20)
        upload_btn.grid(row=9, column=1, pady=10, padx=20)
        back_btn.grid(row=9, column=0, pady=10, padx=20)
        upload_label.grid(row=0, column=0, pady=10, padx=20)
        upload_des.grid(row=0, column=0, pady=10, padx=20)
        upload_label.place(x=325, y=25)
        upload_des.place(x=230, y=70)
        mainFrame.place(x=85, y=120)

        def insert_book():
            check_counter = 0
            warn = ""
            if book_title.get() == "":
                warn = "Title can't be empty"
            else:
                check_counter += 1

            if book_author.get() == "":
                warn = "Author can't be empty"
            else:
                check_counter += 1

            if book_ISBN.get() == "":
                warn = "ISBN can't be empty"
            else:
                check_counter += 1

            if variable.get() == "":
                warn = "Select category"
            else:
                check_counter += 1

            if book_synopsis.get() == "":
                warn = "Synopsis can't be empty"
            else:
                check_counter += 1

            if book_link.get() == "":
                warn = "Please choose a file"
            else:
                check_counter += 1

            if cover_link.get() == "":
                warn = "Please choose a file"
            else:
                check_counter += 1

            if check_counter == 7:
                try:
                    shutil.copy(book_link.get(), '../ALL Project 1/Library/')
                    shutil.copy(cover_link.get(), '../ALL Project 1/Library/BookCover')
                    con = sqlite3.connect('userdata.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO books (title, author, ISBN, synopsis, category, path, cover) VALUES (:title, "
                        ":author, "
                        ":ISBN, :synopsis, :category, :path, :cover)", {
                            'title': book_title.get(),
                            'author': book_author.get(),
                            'ISBN': book_ISBN.get(),
                            'synopsis': book_synopsis.get(),
                            'category': variable.get(),
                            'path': ('../ALL Project 1/Library/' + os.path.basename(self.filename)),
                            'cover': ('../ALL Project 1/Library/BookCover/' + os.path.basename(self.cover_name))

                        })
                    con.commit()
                    messagebox.showinfo('confirmation', 'Book uploaded successfully!')
                    controller.show_frame(MainPage)

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)

        def choose_file():
            self.filename = filedialog.askopenfilename(initialdir='../', title='Select a file',
                                                       filetypes=[('PDF files', '*.pdf')])
            book_link.insert(END, self.filename)

        def choose_cover():
            self.cover_name = filedialog.askopenfilename(initialdir='../', title='Select a file',
                                                         filetypes=[('Image files', '*.jpg *jpeg *.png')])
            cover_link.insert(END, self.cover_name)


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        self.controller = controller

        categories = ['All Categories', 'Action and Adventure', 'Self Improvement', 'Mystery', 'Horror', 'Fantasy',
                      'Sci-Fi', 'Romance', 'Crime', 'History']
        mainFrame = tk.Frame(self)
        top_frame = tk.Frame(self, bg='#CCCCCC')
        sidebar_frame = tk.Frame(self, bg="#CCCCCC", borderwidth=2, relief=RIDGE)

        variable = tk.StringVar()
        variable.set(categories[0])

        book1S = Image.open(coverList[0])
        book1S = book1S.resize((131, 170), Image.ANTIALIAS)
        book1S = ImageTk.PhotoImage(book1S)
        global book1S_label
        book1S_label = tk.Label(self, image=book1S)
        book1S_label.image = book1S
        book1S_label.place(x=225, y=160)
        global book1S_btn
        book1S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 0))
        book1S_btn.place(x=225, y=345)
        book1S_label.pack()
        book1S_btn.pack()

        book2S = Image.open(coverList[1])
        book2S = book2S.resize((131, 170), Image.ANTIALIAS)
        book2S = ImageTk.PhotoImage(book2S)
        global book2S_label
        book2S_label = tk.Label(self, image=book2S)
        book2S_label.image = book2S
        book2S_label.place(x=400, y=160)
        global book2S_btn
        book2S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 1))
        book2S_btn.place(x=400, y=345)
        book2S_label.pack()
        book2S_btn.pack()

        book3S = Image.open(coverList[2])
        book3S = book3S.resize((131, 170), Image.ANTIALIAS)
        book3S = ImageTk.PhotoImage(book3S)
        global book3S_label
        book3S_label = tk.Label(self, image=book3S)
        book3S_label.image = book3S
        book3S_label.place(x=575, y=160)
        global book3S_btn
        book3S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 2))
        book3S_btn.place(x=575, y=345)
        book3S_label.pack()
        book3S_btn.pack()

        book4S = Image.open(coverList[3])
        book4S = book4S.resize((131, 170), Image.ANTIALIAS)
        book4S = ImageTk.PhotoImage(book4S)
        global book4S_label
        book4S_label = tk.Label(self, image=book4S)
        book4S_label.image = book4S
        book4S_label.place(x=225, y=390)
        global book4S_btn
        book4S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 3))
        book4S_btn.place(x=225, y=575)
        book4S_label.pack()
        book4S_btn.pack()

        book5S = Image.open(coverList[4])
        book5S = book5S.resize((131, 170), Image.ANTIALIAS)
        book5S = ImageTk.PhotoImage(book5S)
        global book5S_label
        book5S_label = tk.Label(self, image=book5S)
        book5S_label.image = book5S
        book5S_label.place(x=400, y=390)
        global book5S_btn
        book5S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 4))
        book5S_btn.place(x=400, y=575)
        book5S_label.pack()
        book5S_btn.pack()

        book6S = Image.open(coverList[5])
        book6S = book6S.resize((131, 170), Image.ANTIALIAS)
        book6S = ImageTk.PhotoImage(book6S)
        global book6S_label
        book6S_label = tk.Label(self, image=book6S)
        book6S_label.image = book6S
        book6S_label.place(x=575, y=390)
        global book6S_btn
        book6S_btn = tk.Button(self, width=15, text='View Book',
                               command=lambda: controller.refreshDetail(DetailPage, 5))
        book6S_btn.place(x=575, y=575)
        book6S_label.pack()
        book6S_btn.pack()

        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("sans", 20, 'bold'))

        featured_lbl = tk.Label(self, text="Search results", bg='#BFCACA')
        featured_lbl.config(font=("sans", 18, 'italic'))

        search_lbl = tk.Label(self, text="Search Results", bg='#BFCACA')
        search_lbl.config(font=("sans", 18, 'italic'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.refreshMain(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: log_out())

        def log_out():
            controller.show_frame(LoginPage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')

        global search_entry_side
        search_entry_side = tk.Entry(mainFrame, width=67, font=f)
        search_entry_side.pack(side=LEFT, fill=BOTH, expand=1)
        search_entry_side.insert(0, "Search eBooks by title, author, or ISBN")

        category_filter = tk.OptionMenu(mainFrame, variable, *categories)
        category_filter.pack(side=LEFT)

        search_button = tk.Button(mainFrame, text='Search', command=lambda: controller.refreshSideSearch(SearchPage))
        search_button.pack(side=RIGHT)
        mainFrame.pack(side=TOP)

        recommendations_btn = tk.Button(sidebar_frame, text='Recommendations')
        categories_btn = tk.Button(sidebar_frame, text='Categories')
        chat_btn = tk.Button(sidebar_frame, text='World Chat', command=lambda: Client(HOST, PORT))
        upload_btn = tk.Button(sidebar_frame, text='Upload an eBook', command=lambda: controller.show_frame(UploadPage))

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        recommendations_btn.grid(row=0, column=0, padx=10, pady=5)
        categories_btn.grid(row=1, column=0, padx=10, pady=5)
        chat_btn.grid(row=3, column=0, padx=10, pady=5)
        upload_btn.grid(row=2, column=0, padx=10, pady=5)

        mainFrame.place(x=41, y=70)
        top_frame.place(x=426, y=20)
        sidebar_frame.place(x=40, y=120)
        header_label.place(x=40, y=20)
        featured_lbl.place(x=225, y=120)


app = App()
app.geometry('800x650')
app.title('eBook Reader')
app.resizable(False, False)
app.mainloop()
