def miarka(n):
    skala = '|'
    for i in range(n):
        skala += "....|"

    liczby = '0'
    for i in range(1, n + 1):
        liczby += f"{i:>5}"
    
    return skala + "\n" + liczby

def prostokat(wysokosc, szerokosc):
    pozioma_krawedz = "+---" * szerokosc + "+"
    pionowa_krawedz = "|   " * szerokosc + "|"
    
    grid = ""
    for _ in range(wysokosc):
        grid += pozioma_krawedz + "\n"
        grid += pionowa_krawedz + "\n"
    
    grid += pozioma_krawedz
    return grid

print("MIARKA:")
print(miarka(12))
print("PROSTOKAT:")
print(prostokat(2, 4))