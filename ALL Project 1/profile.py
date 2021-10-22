import tkinter as tk
from PIL import Image, ImageTk

f = ('Arial', 14)

profile_page = tk.Tk()
profile_page.title("eBook Reader - Profile")
profile_page.iconbitmap('ebook.ico')
profile_page.geometry('800x600')
profile_page.config(bg='#BFCACA')

# profile pic
pic = Image.open('profilepic.jpeg')
pic = pic.resize((100, 100), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(pic)
pic_label = tk.Label(image=pic)
pic_label.image = pic
pic_label.place(x=40, y=80)

# details
name_label = tk.Label(profile_page, text="Welcome, User!", bg='#BFCACA')
name_label.config(font=('courier', 20))
name_label.place(x=170, y=100)

# widgets
top_frame = tk.Frame(profile_page, bg='#BFCACA')

header_label = tk.Label(profile_page, text="eBook Reader", bg='#BFCACA')
header_label.config(font=("Verdana", 20, 'bold'))

main_btn = tk.Button(top_frame, text='Main Page')
library_btn = tk.Button(top_frame, text='My Library')
profile_btn = tk.Button(top_frame, text='Profile')
logout_btn = tk.Button(top_frame, text='Log Out')

edit_profile = tk.Button(profile_page, text="Edit Profile")
edit_profile.place(x=180, y=140)


main_btn.grid(row=0, column=0, padx=10, pady=5)
library_btn.grid(row=0, column=1, padx=10, pady=5)
profile_btn.grid(row=0, column=2, padx=10, pady=5)
logout_btn.grid(row=0, column=3, padx=10, pady=5)


top_frame.place(x=426, y=20)
header_label.place(x=40, y=20)

profile_page.mainloop()