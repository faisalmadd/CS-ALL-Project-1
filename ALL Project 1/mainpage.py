from tkinter import *

f = ('Arial', 14)

main_page = Tk()
main_page.title("eBook Reader - Welcome Page")
main_page.iconbitmap('ebook.ico')
main_page.geometry('800x600')
main_page.config(bg='#F44336')

categories = ['All Categories', 'Action and Adventure', 'Comic', 'Mystery', 'Horror', 'Fantasy', 'Sci-Fi']
mainFrame = Frame(main_page)
top_frame = Frame(main_page, bg='white')
sidebar_frame = Frame(main_page, bg="White", borderwidth=2, relief=RIDGE)

variable = StringVar()
variable.set(categories[0])

# widgets
header_label = Label(main_page, text="eBook Reader")
header_label.config(font=("sans", 20, 'bold'))

featured_lbl = Label(main_page, text="Featured Reads", bg='#F44336')
featured_lbl.config(font=("sans", 18, 'italic'))

main_btn = Button(top_frame, text='Main Page')
library_btn = Button(top_frame, text='My Library')
profile_btn = Button(top_frame, text='Profile')
logout_btn = Button(top_frame, text='Log Out')

search_entry = Entry(mainFrame, width=67, font=f)
search_entry.pack(side=LEFT, fill=BOTH, expand=1)
search_entry.insert(0, "Search eBooks by title, author, or ISBN")

category_filter = OptionMenu(mainFrame, variable, *categories).pack(side=LEFT)

search_button = Button(mainFrame, text='Search')
search_button.pack(side=RIGHT)
mainFrame.pack(side=TOP)

recommendations_btn = Button(sidebar_frame, text='Recommendations')
featured_btn = Button(sidebar_frame, text='Featured')
categories_btn = Button(sidebar_frame, text='Categories')
downloaded_btn = Button(sidebar_frame, text='Downloaded eBooks')
upload_btn = Button(sidebar_frame, text='Upload an eBook')

main_btn.grid(row=0, column=0, padx=10, pady=5)
library_btn.grid(row=0, column=1, padx=10, pady=5)
profile_btn.grid(row=0, column=2, padx=10, pady=5)
logout_btn.grid(row=0, column=3, padx=10, pady=5)

recommendations_btn.grid(row=0, column=0, padx=10, pady=5)
featured_btn.grid(row=1, column=0, padx=10, pady=5)
categories_btn.grid(row=2, column=0, padx=10, pady=5)
downloaded_btn.grid(row=3, column=0, padx=10, pady=5)
upload_btn.grid(row=4, column=0, padx=10, pady=5)

mainFrame.place(x=41, y=70)
top_frame.place(x=426, y=20)
sidebar_frame.place(x=40, y=120)
header_label.place(x=40, y=20)
featured_lbl.place(x=225, y=120)

main_page.mainloop()
