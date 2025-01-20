import sqlite3

def create_database():
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        creator TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        status_reading TEXT NOT NULL DEFAULT 'jeszcze nie czytana',
                        rating TEXT DEFAULT NULL
                    )''')
    connection.commit()
    connection.close()

def insert_book(title, genre, creator, year):
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books (title, genre, creator, year) VALUES (?, ?, ?, ?)",
                   (title, genre, creator, year))
    connection.commit()
    connection.close()

def delete_book(book_id):
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()

def search_book(query):
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR creator LIKE ?", (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    connection.close()
    return results

def list_books():
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    connection.close()
    return results

def update_book_status(book_id, new_status):
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET status_reading = ? WHERE id = ?", (new_status, book_id))
    connection.commit()
    connection.close()

def rate_book(book_id, rating):
    connection = sqlite3.connect("books_database.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET rating = ? WHERE id = ?", (rating, book_id))
    connection.commit()
    connection.close()