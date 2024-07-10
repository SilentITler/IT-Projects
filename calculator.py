import os

print("Willkommen zu deinem Taschenrechner")


def addition(a, b):
    return a + b


def subtraktion(a, b):
    return a - b


def multiplikation(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Teilen durch null geht nicht"


mehr = "ja"

while mehr == "ja":
    print("Wähle")
    print("1 Additon")
    print("2 Subtraktion")
    print("3 Multiplikation")
    print("4 Division")

    wahl = input("Was soll gemacht werden (1/2/3/4): ")

    zahl1 = float(input("Eingabe erste Zahl: "))
    Zahl2 = float(input("Eingabe zweite Zahl: "))

    
    if wahl == 1:
            ergebnis = addition(zahl1, Zahl2)
            print(f"Ergebnis von {zahl1} + {Zahl2} = {ergebnis}")
    elif wahl == 2:
            ergebnis = subtraktion(zahl1, Zahl2)
            print(f"Ergebnis von {zahl1} - {Zahl2} = {ergebnis}")
    elif wahl == 3:
            ergebnis = multiplikation(zahl1, Zahl2)
            print(f"Ergebnis von {zahl1} * {Zahl2} = {ergebnis}")
    elif wahl == 4:
            ergebnis = division(zahl1, Zahl2)
            print(f"Ergebnis von {zahl1} / {Zahl2} = {ergebnis}")
else:
        print("Ungültige Wahl. Bitte wählen Sie nur zwischen 1, 2, 3 oder 4.")

    
mehr = input("Möchtest du mehr Berechnungen durchführen? (ja/nein): ")

print("Vielen Dank für die Verwendung des Taschenrechners. Auf Wiedersehen!")
