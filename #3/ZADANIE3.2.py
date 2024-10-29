L = [3, 5, 4] ; L = L.sort()

print(L)
#funkcja zwraca NONE - poprawnie byłoby:
#L = [3, 5, 4]
#L.sort()

x, y = 1, 2, 3
#nie możemy przypisać 3 wartości do tylko 2 zmiennych

X = 1, 2, 3 ; X[1] = 4
#X nie jest listą, nie możemy zmieniać elementów X

X = [1, 2, 3] ; X[3] = 4
#brak indeksu 3, indeksy są tylko od 0 do 2

X = "abc" ; X.append("d")
#obiekty str nie mają metody append

L = list(map(pow, range(8)))
#funkcja pow() powinna otrzymać dwa argumenty: bazę i wykładnik.