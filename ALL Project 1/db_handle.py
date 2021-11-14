import random
import shutil
import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

idList = []
coverList = []
titleList = []
authorList = []
synopsisList = []
pathList = []
reviewList = []
ratingList = []
currentBook = []
ran6 = random.sample(range(1, 21), 6)
searchTitle = []
searchAuthor = []
searchISBN = []


def readBookID(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookID = bookRecord[0]
    return bookID


def readCoverFile(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    coverFile = bookRecord[7]
    return coverFile


def readBookTitle(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookTitle = bookRecord[1]
    return bookTitle


def readBookAuthor(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookAuthor = bookRecord[2]
    return bookAuthor


def readBookSynopsis(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookSynopsis = bookRecord[4]
    return bookSynopsis


def readBookPath(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * from books where book_id = ?"
    cursor.execute(query, (bookID,))
    bookRecord = cursor.fetchone()
    bookPath = bookRecord[6]
    return bookPath


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
    reviewList.clear()
    ratingList.clear()

    for x in ran6:
        idList.append(readBookID(x))
        coverList.append(readCoverFile(x))
        titleList.append(readBookTitle(x))
        authorList.append(readBookAuthor(x))
        synopsisList.append(readBookSynopsis(x))
        pathList.append(readBookPath(x))
        reviewList.append(get_review(x))
        ratingList.append(get_rating(x))


def search(q):
    searchTitle.clear()
    searchAuthor.clear()
    searchISBN.clear()
    idList.clear()
    coverList.clear()
    titleList.clear()
    authorList.clear()
    synopsisList.clear()
    pathList.clear()
    reviewList.clear()
    ratingList.clear()

    qNew = "%" + q + "%"

    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()

    queryID = "SELECT * from books where title LIKE ?"
    cursor.execute(queryID, (qNew,))
    bookRecord = cursor.fetchall()
    for row in bookRecord:
        searchTitle.append(row[0])

    queryID = "SELECT * from books where author LIKE ?"
    cursor.execute(queryID, (qNew,))
    bookRecord = cursor.fetchall()
    for row in bookRecord:
        searchAuthor.append(row[0])

    queryID = "SELECT * from books where ISBN LIKE ?"
    cursor.execute(queryID, (q,))
    bookRecord = cursor.fetchall()
    for row in bookRecord:
        searchAuthor.append(row[0])

    a = set(searchTitle)
    b = set(searchAuthor)
    c = set(searchISBN)

    searchResultList = list(a.union(b, c))
    for x in searchResultList:
        idList.append(readBookID(x))
        coverList.append(readCoverFile(x))
        titleList.append(readBookTitle(x))
        authorList.append(readBookAuthor(x))
        synopsisList.append(readBookSynopsis(x))
        pathList.append(readBookPath(x))
        reviewList.append(get_review(x))
        ratingList.append(get_rating(x))

    print(titleList)


def get_review(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * FROM reviews WHERE book_id = ?"
    cursor.execute(query, (bookID,))
    reviewsRecord = cursor.fetchone()
    bookReview = reviewsRecord[0]
    return bookReview


def get_rating(bookID):
    con = sqlite3.connect('ebook_db.db')
    cursor = con.cursor()
    query = "SELECT * FROM reviews WHERE book_id = ?"
    cursor.execute(query, (bookID,))
    ratingRecord = cursor.fetchone()
    bookRating = ratingRecord[1]
    return bookRating


randomLists()
