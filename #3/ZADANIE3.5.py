def miarka(dlugosc):
    skala = '|'
    for i in range(dlugosc):
        skala += "....|"
       
    liczby = '0'
    for i in range(1, dlugosc + 1):
        liczby += f"{i:>5}"
    
    print(skala)
    print(liczby)

miarka(12)