from math import ceil
from turtle import forward, right, left, speed, circle, setpos, penup, pendown, exitonclick
speed(10)                                  # Rychlost vykreslování

sloupce=int(input("Počet sloupců: "))      # Počet sloupců mřížky
while sloupce<=0:                          # Číslo nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        sloupce=int(input("Počet sloupců: "))
radky=int(input("Počet řádků: "))          # Počet řádků mřížky
while radky<=0:                            # Číslo nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        radky=int(input("Počet sloupců: "))
strana=50                                  # Velikost strany jednoho čtverce v mřížce

for k in range (radky):                    # Nakreslí tabulku    
    for j in range(sloupce):               # Nakreslí řádek        
        for i in range(4):                 # Nakreslí čtverec
            forward(strana)
            right(90)
        forward(strana)
    left(180)
    forward(sloupce*strana)
    left(90)
    forward(strana)
    left(90)
penup()                                    # Zvednutí tužky, přerušení psaní

tahy=(ceil((sloupce*radky)/2))             # Maximální počet tahů
pocet_tahu=0                               # Počítadlo tahů

for l in range(tahy):                      # Nakreslí křížky a kolečka
    print("Na tahu je první hráč")
    cislo_sloupce=int(input("Sloupec: "))               # První hráč zadá číslo sloupce, do kterého chce nakreslit křížek
    while cislo_sloupce>sloupce or cislo_sloupce<=0:    # Číslo nesmí být vyšší, než je počet sloupců a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        cislo_sloupce=int(input("Sloupec: "))
    
    cislo_radku=int(input("Řádek: "))                   # První hráč zadá číslo řádku, do kterého chce nakreslit křížek
    while cislo_radku>radky or cislo_radku<=0:          # Číslo nesmí být vyšší, než je počet řádků a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        cislo_radku=int(input("Řádek: "))

    setpos(cislo_sloupce*strana-strana/2, -cislo_radku*strana+strana/2)       # Souřadnice políčka v mřížce
    pendown()                       # Položení tužky, pokračování ve psaní
    for m in range(4):              # Nakreslení křížku
        left(45)
        forward(strana/2-5)
        left(180)
        forward(strana/2-5)
        left(45)
    penup()

    pocet_tahu=pocet_tahu+1         # Přičtení tahu
    if pocet_tahu==sloupce*radky:   # Pokud se počet tahů rovná počtu polí, hra skončí
        break

    print("Na tahu je druhý hráč")
    cislo_sloupce=int(input("Sloupec: "))                   # Druhý hráč zadá číslo sloupce, do kterého chce nakreslit kolečko
    while cislo_sloupce>sloupce or cislo_sloupce<=0:        # Číslo nesmí být vyšší, než je počet sloupců a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        cislo_sloupce=int(input("Sloupec: "))

    cislo_radku=int(input("Řádek: "))                       # Druhý hráč zadá číslo řádku, do kterého chce nakreslit kolečko
    while cislo_radku>radky or cislo_radku<=0:              # Číslo nesmí být vyšší, než je počet řádků a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        cislo_radku=int(input("Řádek: "))

    setpos(cislo_sloupce*strana-strana/2, -cislo_radku*strana+5)        # Nakreslení kolečka
    pendown()
    circle(strana/2-5)
    penup()
    
    pocet_tahu=pocet_tahu+1         # Přičtení tahu
    if pocet_tahu==sloupce*radky:
        break

print("Pěkná hra!")

exitonclick()                       # Okno se samo nezavře