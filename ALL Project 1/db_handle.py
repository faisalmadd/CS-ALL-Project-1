import sqlite3


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

