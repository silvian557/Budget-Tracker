print("Bun venit!")
print("Program - Budget Tracker")
print("-" * 50)

buget = 0.0
total_cheltuit = 0.0

while True:
    try:
        buget = float(input("Introdu bugetul tau initial (lei) - "))
        if buget < 0:
            print("Bugetul nu poate fi negativ! Incearca din nou")
        else:
            break
    except ValueError:
        print("Eroare! Introdu doar cifre")

while True:
    print("-" * 50)
    print("1. Adauga o cheltuiala")
    print("2. Vezi situatia banilor")
    print("3. Iesire program")

    alegere_user = int(input("Ce optiune alegi (1, 2 sau 3)? - "))

    if alegere_user == 1:
        nume = input("Numele cheltuielii - ")
        
        while True:
            try:
                suma = float(input("Cat a costat - "))
                if suma <= 0:
                    print("Suma trebuie sa fie mai mare ca 0!")
                elif suma > buget:
                    print("Nu ai destui bani in buget!")
                    break
                else:
                    buget = buget - suma
                    total_cheltuit = total_cheltuit + suma
                    print("Cheltuiala adaugata cu succes!")
                    break
            except ValueError:
                print("Eroare! Introdu o suma valida")

    elif alegere_user == 2:
        print("--- SITUATIE FINANCIARA ---")
        print("Bani ramasi in buget:", buget, "lei")
        print("Total cheltuit pana acum:", total_cheltuit, "lei")

    elif alegere_user == 3:
        print("La revedere!")
        break

    else:
        print("Alege o optiune valida (1, 2 sau 3)!")
