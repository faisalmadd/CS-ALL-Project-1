import os
import shutil
import sqlite3
import tkinter as tk
from tkinter import SOLID, N, messagebox, W, LEFT, RIDGE, BOTH, RIGHT, TOP, filedialog, END, scrolledtext
from PIL import Image, ImageTk
from chatclient import Client
import PyPDF2

f = ('Arial', 14)
ENCODING = 'utf-8'
HOST = '127.0.0.1'
PORT = 8080


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, LoginPage, RegistrationPage, MainPage, ProfilePage, UploadPage, DetailPage, MyLibrary,
                  ReaderPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
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

        categories = ['All Categories', 'Action and Adventure', 'Self Improvement', 'Mystery', 'Horror', 'Fantasy',
                      'Sci-Fi']
        mainFrame = tk.Frame(self)
        top_frame = tk.Frame(self, bg='#CCCCCC')
        sidebar_frame = tk.Frame(self, bg="#CCCCCC", borderwidth=2, relief=RIDGE)

        variable = tk.StringVar()
        variable.set(categories[0])

        # widgets
        book1 = Image.open('../ALL Project 1/Library/BookCover/robinson_crusoe.jpg')
        book1 = book1.resize((131, 170), Image.ANTIALIAS)
        book1 = ImageTk.PhotoImage(book1)
        book1_label = tk.Label(self, image=book1)
        book1_label.image = book1
        book1_label.place(x=225, y=160)
        book1_btn = tk.Button(self, width=15, text='View Book', command=lambda: controller.show_frame(DetailPage))
        book1_btn.place(x=225, y=345)

        book2 = Image.open('../ALL Project 1/Library/BookCover/the_valley_of_fear.jpeg')
        book2 = book2.resize((131, 170), Image.ANTIALIAS)
        book2 = ImageTk.PhotoImage(book2)
        book2_label = tk.Label(self, image=book2)
        book2_label.image = book2
        book2_label.place(x=400, y=160)
        book2_btn = tk.Button(self, width=15, text='View Book')
        book2_btn.place(x=400, y=345)

        book3 = Image.open('../ALL Project 1/Library/BookCover/time_management.jpeg')
        book3 = book3.resize((131, 170), Image.ANTIALIAS)
        book3 = ImageTk.PhotoImage(book3)
        book3_label = tk.Label(self, image=book3)
        book3_label.image = book3
        book3_label.place(x=575, y=160)
        book3_btn = tk.Button(self, width=15, text='View Book')
        book3_btn.place(x=575, y=345)

        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("sans", 20, 'bold'))

        featured_lbl = tk.Label(self, text="Featured Reads", bg='#BFCACA')
        featured_lbl.config(font=("sans", 18, 'italic'))

        main_btn = tk.Button(top_frame, text='Main Page', state='disabled')
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: controller.show_frame(LoginPage))

        search_entry = tk.Entry(mainFrame, width=67, font=f)
        search_entry.pack(side=LEFT, fill=BOTH, expand=1)
        search_entry.insert(0, "Search eBooks by title, author, or ISBN")

        category_filter = tk.OptionMenu(mainFrame, variable, *categories)
        category_filter.pack(side=LEFT)

        search_button = tk.Button(mainFrame, text='Search')
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


class DetailPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.show_frame(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: controller.show_frame(LoginPage))

        book1 = Image.open('../ALL Project 1/Library/BookCover/robinson_crusoe.jpg')
        book1 = book1.resize((131, 170), Image.ANTIALIAS)
        book1 = ImageTk.PhotoImage(book1)
        book1_label = tk.Label(self, image=book1)
        book1_label.image = book1
        book1_label.place(x=40, y=80)

        title_label = tk.Label(self, bg='#BFCACA', text='Robinson Crusoe')
        title_label.config(font=("Sans", 20, 'bold'))
        author_label = tk.Label(self, bg='#BFCACA', text='Daniel Defoe')
        author_label.config(font=("Sans", 20, 'bold'))
        synopsis_label = tk.Message(self, bg='#BFCACA', width=400, text="Robinson Crusoe is a novel by Daniel Defoe, "
                                                                        "first published on 25 April 1719. The first "
                                                                        "edition credited the work's protagonist "
                                                                        "Robinson Crusoe as its author, leading many "
                                                                        "readers to believe he was a real person and "
                                                                        "the book a travelogue of true incidents.")
        synopsis_label.config(font=("Sans", 16, 'italic'))
        title_label.place(x=200, y=80)
        author_label.place(x=200, y=110)
        synopsis_label.place(x=200, y=150)

        review_label = tk.Label(self, bg='#BFCACA', text='Ratings & Reviews')
        review_label.config(font=("Sans", 20, 'bold'))
        review_label.place(x=40, y=275)

        read_btn = tk.Button(self, width=15, text='Begin Reading', command=lambda: controller.show_frame(ReaderPage))
        add_fav = tk.Button(self, width=15, text='Add to My Library')
        download_btn = tk.Button(self, width=15, text='Download')

        read_btn.place(x=625, y=120)
        add_fav.place(x=625, y=160)
        download_btn.place(x=625, y=200)

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)


class ReaderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.show_frame(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: controller.show_frame(LoginPage))

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)

        book_text = tk.scrolledtext.ScrolledText(self, height=35, width=98)
        book_text.place(x=40, y=80)

        pdf_file = PyPDF2.PdfFileReader('../ALL Project 1/Library/Robinson_Crusoe.pdf')
        pages = pdf_file.getNumPages()
        for page_number in range(pages):
            page = pdf_file.getPage(page_number)
            content = page.extractText()
            book_text.insert(1.0, content)


class MyLibrary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.show_frame(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', state='disabled')
        profile_btn = tk.Button(top_frame, text='Profile', command=lambda: controller.show_frame(ProfilePage))
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: controller.show_frame(LoginPage))

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#BFCACA')
        top_frame = tk.Frame(self, bg='#CCCCCC')
        header_label = tk.Label(self, text="eBook Reader", bg='#BFCACA')
        header_label.config(font=("Sans", 20, 'bold'))

        main_btn = tk.Button(top_frame, text='Main Page', command=lambda: controller.show_frame(MainPage))
        library_btn = tk.Button(top_frame, text='My Library', command=lambda: controller.show_frame(MyLibrary))
        profile_btn = tk.Button(top_frame, text='Profile', state='disabled')
        logout_btn = tk.Button(top_frame, text='Log Out', command=lambda: controller.show_frame(LoginPage))

        # profile pic
        pic = Image.open('profilepic.jpeg')
        pic = pic.resize((100, 100), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        pic_label = tk.Label(self, image=pic)
        pic_label.image = pic
        pic_label.place(x=40, y=80)

        # details
        name_label = tk.Label(self, text="Welcome, User!", bg='#BFCACA')
        name_label.config(font=('courier', 20))
        name_label.place(x=170, y=100)

        edit_profile = tk.Button(self, text="Edit Profile")
        edit_profile.place(x=180, y=140)

        main_btn.grid(row=0, column=0, padx=10, pady=5)
        library_btn.grid(row=0, column=1, padx=10, pady=5)
        profile_btn.grid(row=0, column=2, padx=10, pady=5)
        logout_btn.grid(row=0, column=3, padx=10, pady=5)

        top_frame.place(x=426, y=20)
        header_label.place(x=40, y=20)


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
                            path text
                        )
                    ''')
        con.commit()

        tk.Frame.__init__(self, parent, bg='#BFCACA')
        categories = ['Action and Adventure', 'Self Improvement', 'Mystery', 'Horror', 'Fantasy', 'Sci-Fi']
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

        book_title = tk.Entry(mainFrame, font=f, width=50)

        book_author = tk.Entry(mainFrame, font=f, width=50)

        book_ISBN = tk.Entry(mainFrame, font=f, width=50)

        book_synopsis = tk.Entry(mainFrame, font=f, width=50)

        book_category = tk.OptionMenu(mainFrame, variable, *categories)
        book_category.config(width=62, font=('Times', 12))

        book_link = tk.Entry(mainFrame, font=f, width=50)

        choose_btn = tk.Button(mainFrame, width=50, text='Choose a file to upload', font=f, relief=SOLID,
                               cursor='hand2', command=lambda: choose_file())

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

        choose_btn.grid(row=6, column=1, pady=10, padx=20)
        upload_btn.grid(row=7, column=1, pady=10, padx=20)
        back_btn.grid(row=7, column=0, pady=10, padx=20)
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

            if check_counter == 6:
                try:
                    shutil.copy(book_link.get(), '../ALL Project 1/Library/')
                    con = sqlite3.connect('userdata.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO books (title, author, ISBN, synopsis, category, path) VALUES (:title, :author, "
                        ":ISBN, :synopsis, :category, :path)", {
                            'title': book_title.get(),
                            'author': book_author.get(),
                            'ISBN': book_ISBN.get(),
                            'synopsis': book_synopsis.get(),
                            'category': variable.get(),
                            'path': ('../ALL Project 1/Library/' + os.path.basename(self.filename))

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


app = App()
app.geometry('800x600')
app.title('eBook Reader')
app.resizable(False, False)
app.mainloop()
