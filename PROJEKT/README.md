# Baza danych książek

<h2>Opis Projektu</h2>

<p>
Projekt "Baza danych książek" to aplikacja umożliwiająca zarządzanie kolekcją książek. Oferuje interfejs graficzny, który pozwala na:
</p>
<ul>
  <li>Dodawanie książek do bazy.</li>
  <li>Usuwanie książek z bazy.</li>
  <li>Wyszukiwanie książek po tytule lub autorze.</li>
  <li>Wyświetlanie wszystkich książek.</li>
  <li>Zmianę statusu czytania książek.</li>
  <li>Ocenianie książek.</li>
  <li>Eksportowanie danych o książkach do plików w formatach TXT, CSV lub JSON.</li>
  <li>Wyjście z aplikacji.</li>
</ul>
<p>
Interfejs użytkownika został zbudowany przy użyciu biblioteki `tkinter` w Pythonie, a baza danych opiera się na SQLite.
</p>

---

<h2>Wymagania</h2>

<ul>
  <li>Python 3.10 lub nowszy</li>
  <li>Biblioteka <code>tkinter</code></li>
  <li>Biblioteka <code>sqlite3</code></li>
</ul>

---

<h2>Instalacja</h2>

<ol>
  <li>Sklonuj repozytorium:
    <pre><code>git clone https://github.com/xxMegi/Python.git</code></pre>
  </li>
  <li>Przejdź do katalogu projektu:
    <pre><code>cd PROJEKT</code></pre>
  </li>
  <li>Uruchom aplikację:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

---

<h2>Funkcjonalności</h2>

<h3>1.Dodawanie Książek</h3>
<p>Wprowadź tytuł, gatunek, autora i rok wydania książki. Kliknij przycisk Wstaw książkę, aby dodać ją do bazy danych.</p>

<h3>2.Usuwanie Książek</h3>
<p>Podaj ID książki, którą chcesz usunąć, i kliknij przycisk Usuń książkę.</p>

<h3>3.Wyszukiwanie Książek</h3>
<p>Wprowadź tytuł lub autora i kliknij Znajdź książkę, aby wyświetlić pasujące wyniki.</p>

<h3>4.Wyświetlanie Wszystkich Książek</h3>
<p>Kliknij przycisk Pokaż wszystkie książki, aby zobaczyć pełną listę książek w bazie wraz z statusem ich czytania i oceną.</p>

<h3>5.Zmiana Statusu Czytania</h3>
<p>Podaj ID książki i nowy status (np. "jeszcze nie czytana", "w trakcie czytania", "przeczytana"), a następnie kliknij Zmień status czytania książki.</p>

<h3>6.Ocenianie Książek</h3>
<p>Podaj ID książki i ocenę w formie gwiazdek (np. ***, ****, *****), a następnie kliknij Oceń książkę.</p>

<h3>7.Eksportowanie Danych</h3>
<p>Wybierz format pliku (TXT, CSV lub JSON) i kliknij Eksportuj do pliku, aby zapisać dane o książkach w wybranym formacie.</p>

---

<h2>Struktura Plików</h2>

<ul>
  <li><code>database.py</code>: Moduł odpowiedzialny za operacje na bazie danych, takie jak dodawanie, usuwanie, wyszukiwanie, aktualizowanie statusu czytania i ocenianie książek.</li>
  <li><code>export.py</code>: Główny moduł aplikacji, zawierający interfejs użytkownika oparty na <code>tkinter</code>.</li>
  <li><code>export.py</code>: Moduł eksportujący dane o książkach do plików w formatach TXT, CSV lub JSON.</li>   
  <li><code>README.md</code>: Dokumentacja projektu.</li>
</ul>

---

<h2>Przykładowy Widok</h2>

<p>
Po uruchomieniu aplikacji użytkownik zobaczy okno z:
</p>
<ul>
  <li>Przyciskiem dla każdej z funkcjonalności.</li>
  <li>Polem tekstowym do wprowadzania danych (np. tytułu, autora).</li>
  <li>Obszarem graficznym do wyświetlania wyników wyszukiwania i listy książek.</li>
</ul>

---

<h2>Autor</h2>

<b>Magdalena Kiszka</b>

