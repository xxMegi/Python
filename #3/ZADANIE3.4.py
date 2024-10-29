while True:

    user_input = input("Podaj liczbę rzeczywistą lub wpisz 'stop' aby zakończyć: ")
    
    if user_input.lower() == "stop":
        break
    
    try:
        x = float(user_input)
        print(f"Liczba: {x}, trzecia potęga liczby: {x**3}")
    except ValueError:
        print("Błąd: Podana wartość nie jest liczbą")
