from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Arial', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books(
                    book_id number,
                    title text, 
                    author text,
                    ISBN number, 
                    synopsis text, 
                    category text
                )
            ''')
con.commit()

upload_page = Tk()
upload_page.title("eBook Reader - Upload Page")
upload_page.geometry('800x600')
upload_page.config(bg='#F44336')

categories = ['All Categories', 'Action and Adventure', 'Comic', 'Mystery', 'Horror', 'Fantasy', 'Sci-Fi']
variable = StringVar()
variable.set(categories[0])

# widget
upload_label = Label(upload_page, text="Upload Page", bg='#F44336')
upload_label.config(font=("Arial", 20))

upload_des = Label(upload_page, text="Upload your eBooks to the eReader!", bg='#F44336')
upload_des.config(font=("Arial", 18))

right_frame = Frame(upload_page, bd=0, bg='#F44336', relief=RIDGE, padx=10, pady=10)

title_label = Label(right_frame, text="Title", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)

author_label = Label(right_frame, text="Author", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)

ISBN_label = Label(right_frame, text="ISBN", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)

synopsis_label = Label(right_frame, text="Synopsis", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)

category_label = Label(right_frame, text="Category", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)

file_label = Label(right_frame, text="Upload File", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)

book_title = Entry(right_frame, font=f, width=50)

book_author = Entry(right_frame, font=f, width=50)

book_ISBN = Entry(right_frame, font=f, width=50)

book_synopsis = Entry(right_frame, font=f, width=50)

book_category = OptionMenu(right_frame, variable, *categories)
book_category.config(width=62, font=('Times', 12))

choose_btn = Button(right_frame, width=50, text='Choose a file to upload', font=f, relief=SOLID, cursor='hand2')

upload_btn = Button(right_frame, width=50, text='Upload book!', bg='green', font=f, relief=SOLID, cursor='hand2')

back_btn = Button(right_frame, text='Back to main page', font=f, relief=SOLID, cursor='hand2')

book_title.grid(row=0, column=1, pady=10, padx=20)
book_author.grid(row=1, column=1, pady=10, padx=20)
book_ISBN.grid(row=2, column=1, pady=10, padx=20)
book_synopsis.grid(row=3, column=1, pady=10, padx=20)
book_category.grid(row=4, column=1, pady=10, padx=20)

choose_btn.grid(row=5, column=1, pady=10, padx=20)
upload_btn.grid(row=7, column=1, pady=10, padx=20)
back_btn.grid(row=7, column=0, pady=10, padx=20)
upload_label.grid(row=0, column=0, pady=10, padx=20)
upload_des.grid(row=0, column=0, pady=10, padx=20)
upload_label.place(x=350, y=20)
upload_des.place(x=260, y=70)
right_frame.place(x=100, y=120)

upload_page.mainloop()
