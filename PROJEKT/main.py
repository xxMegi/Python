import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from database import create_database, insert_book, delete_book, search_book, list_books, update_book_status, rate_book
from export import export_to_file


class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twoja Baza Książek")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffe6f2") 
        self.menu_frame = tk.Frame(self.root, bg="#ffe6f2")
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            self.menu_frame, 
            text="Witaj w Bazie Książek", 
            font=("Calibri", 20, "bold"), 
            bg="#ffe6f2", 
            fg="black"
        ).pack(pady=20)

        button_style = {"font": ("Calibri", 14), "bg": "#ffccdd", "fg": "black", "activebackground": "#ff99bb"}

        tk.Button(self.menu_frame, text="Wstaw książkę", command=self.add_book, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Usuń książkę", command=self.delete_book, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Znajdź książkę", command=self.search_books, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Pokaż wszystkie książki", command=self.show_books, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Zmień status czytania książki", command=self.change_status, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Oceń książkę", command=self.rate_book, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Eksportuj do pliku", command=self.export_data, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Wyjście", command=self.root.quit, **button_style).pack(fill=tk.X, pady=5)

        create_database()

    def add_book(self):
        title = simpledialog.askstring("Dodaj książkę", "Wpisz tytuł:")
        genre = simpledialog.askstring("Dodaj książkę", "Wpisz gatunek:")
        creator = simpledialog.askstring("Dodaj książkę", "Wpisz autora:")
        year = simpledialog.askinteger("Dodaj książkę", "Wpisz rok:")
        
        if title and genre and creator and year:
            insert_book(title, genre, creator, year)
            messagebox.showinfo("Sukces", "Książka została dodana.")
        else:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione!")

    def delete_book(self):
        book_id = simpledialog.askinteger("Usuń książkę", "Wpisz ID książki do usunięcia:")
        if book_id:
            delete_book(book_id)
            messagebox.showinfo("Sukces", "Książka została usunięta.")
        else:
            messagebox.showerror("Błąd", "Musisz podać poprawne ID!")

    def search_books(self):
        query = simpledialog.askstring("Znajdź książkę", "Wpisz tytuł lub autora:")
        if query:
            results = search_book(query)
            self.display_books(results)
        else:
            messagebox.showerror("Błąd", "Musisz podać zapytanie!")

    def show_books(self):
        results = list_books()
        self.display_books(results)

    def display_books(self, books):
        book_window = tk.Toplevel(self.root)
        book_window.title("Lista Książek")
        book_window.geometry("1400x300")

        tree = ttk.Treeview(book_window, columns=("ID", "Tytuł", "Gatunek", "Autor", "Rok", "Status", "Ocena"), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        for col in ("ID", "Tytuł", "Gatunek", "Autor", "Rok", "Status", "Ocena"):
            tree.heading(col, text=col)

        for book in books:
            tree.insert("", tk.END, values=book)

    def change_status(self):
        book_id = simpledialog.askinteger("Zmień status", "Wpisz ID książki:")
        if not book_id:
            messagebox.showerror("Błąd", "Musisz podać ID książki!")
            return

        status = simpledialog.askstring("Zmień status", "Podaj nowy status (jeszcze nie czytana, w trakcie czytania, przeczytana):")
        if status:
            update_book_status(book_id, status)
            messagebox.showinfo("Sukces", "Status książki został zaktualizowany.")
        else:
            messagebox.showerror("Błąd", "Musisz podać nowy status!")

    def rate_book(self):
        book_id = simpledialog.askinteger("Oceń książkę", "Wpisz ID książki:")
        if not book_id:
            messagebox.showerror("Błąd", "Musisz podać ID książki!")
            return

        rating = simpledialog.askstring("Oceń książkę", "Podaj ocenę (1-5 gwiazdek, np. *****):")
        if rating and 1 <= len(rating) <= 5 and rating.count('*') == len(rating):
            rate_book(book_id, rating)
            messagebox.showinfo("Sukces", "Książka została oceniona.")
        else:
            messagebox.showerror("Błąd", "Nieprawidłowa ocena! Wpisz od 1 do 5 gwiazdek.")

    def export_data(self):
        file_format = simpledialog.askstring("Eksport", "Podaj format pliku (txt, csv, json):").lower()
        if file_format in ["txt", "csv", "json"]:
            data = list_books()
            export_to_file(file_format, data)
            messagebox.showinfo("Sukces", f"Dane wyeksportowane do books_database.{file_format}")
        else:
            messagebox.showerror("Błąd", "Nieobsługiwany format pliku!")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()