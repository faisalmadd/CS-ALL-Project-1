from tkinter import *

f = ('Arial', 14)

main_page = Tk()
main_page.title("eBook Reader - Welcome Page")
main_page.iconbitmap('ebook.ico')
main_page.geometry('800x600')
main_page.config(bg='#FFFFFF')

categories = ['All Categories', 'Action and Adventure', 'Comic', 'Mystery', 'Horror', 'Fantasy', 'Sci-Fi']
mainFrame = Frame(main_page)

variable = StringVar()
variable.set(categories[0])

# widgets
header_label = Label(main_page, text="eBook Reader", bg='#FFFFFF')
header_label.config(font=("OpenSans", 20))

search_entry = Entry(mainFrame, width=65, font=f)
search_entry.pack(side=LEFT, fill=BOTH, expand=1)
search_entry.insert(0, "Search eBooks by title, author, or ISBN")

category_filter = OptionMenu(mainFrame, variable, *categories).pack(side=LEFT)

search_button = Button(mainFrame, text='Search')
search_button.pack(side=RIGHT)
mainFrame.pack(side=TOP)

mainFrame.place(x=41, y=60)
header_label.place(x=40, y=20)

main_page.mainloop()
