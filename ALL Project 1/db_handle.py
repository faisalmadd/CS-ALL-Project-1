import random
import shutil
import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


def readBookID(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookID = bookRecord[0]
    return bookID


def readCoverFile(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    coverFile = bookRecord[7]
    return coverFile


def readBookTitle(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookTitle = bookRecord[1]
    return bookTitle


def readBookAuthor(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookAuthor = bookRecord[2]
    return bookAuthor


def readBookSynopsis(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookSynopsis = bookRecord[4]
    return bookSynopsis


def readBookPath(bookID):
    con = sqlite3.connect('userdata.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookPath = bookRecord[6]
    return bookPath


idList = []


coverList = []
titleList = []
authorList = []
synopsisList = []
pathList = []

currentBook = []


ran6 = random.sample(range(1, 21), 6)

def setCurrentBook(x):
    currentBook.clear()
    currentBook.append(x)

def download_book(idx):
    book_path = pathList[idx]
    folder = filedialog.askdirectory()
    shutil.copy(book_path, folder)
    messagebox.showinfo('Download Status', 'Book downloaded successfully!')


def randomLists():
    ran6 = random.sample(range(1, 21), 6)
    idList.clear()
    coverList.clear()
    titleList.clear()
    authorList.clear()
    synopsisList.clear()
    pathList.clear()
    for x in ran6:
        idList.append(readBookID(x))
        coverList.append(readCoverFile(x))
        titleList.append(readBookTitle(x))
        authorList.append(readBookAuthor(x))
        synopsisList.append(readBookSynopsis(x))
        pathList.append(readBookPath(x))


randomLists()

for x in ran6:
    coverList.append(readCoverFile(x))
    titleList.append(readBookTitle(x))
    authorList.append(readBookAuthor(x))
    synopsisList.append(readBookSynopsis(x))
    pathList.append(readBookPath(x))
