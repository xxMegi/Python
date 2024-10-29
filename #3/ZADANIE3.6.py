def prostokat(wysokosc, szerokosc):
    pozioma_krawedz = "+---" * szerokosc + "+"
    pionowa_krawedz = "|   " * szerokosc + "|"
    
    for _ in range(wysokosc):
        print(pozioma_krawedz)
        print(pionowa_krawedz)
    
    print(pozioma_krawedz)

prostokat(2, 4)
