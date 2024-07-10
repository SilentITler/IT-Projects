# Das folgende Programm berechnet nach Benutzereingabe die Primzahlen
# Es ist ein kleiner Fehler im "UI" und die Effizienz lässt zu wünschen übrig.

# Macht den Code schneller -> ABER sucht nicht im Internet mach der Lösung!!!

theprimnumbers = []
yesno="N"
while yesno != "Y":
    inp = int(input("Bis wohin soll ich nach Primzahlen suchen?"))
    if inp > 1000 and inp < 10000:
        yesno = input("Das wird ein bisschen dauern. Bist Du sicher?")
    elif inp > 10000:
        yesno = input("Das wird sehr lange dauern. Bist Du sicher?")
    else:
        yesno = "Y"
        
# es ist eine Primzahl, wenn die Zahl größer als 1 und nur durch sich selbst und durch 1 teilbar ist
# wir fangen bei der Zahl 2 an
for numb in range(2, inp+1):
    prim = True
    for div in range(2, numb):
        if numb % div == 0:  # keine Primzahl
            prim = False
            break
    if prim==True:
        theprimnumbers.insert(0, numb)
        
print(f"Die gefundenen Primzahlen bis {inp} sind: ")
for z in theprimnumbers:
    print(z)
