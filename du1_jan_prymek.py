from math import ceil
from turtle import forward, right, left, speed, circle, setpos, penup, pendown, exitonclick
speed(10)                           # Rychlost vykreslování

a=int(input("Počet sloupců: "))     # Počet sloupců mřížky
b=int(input("Počet řádků: "))       # Počet řádků mřížky
strana=50                           # Velikost strany jednoho čtverce v mřížce

for k in range (b):                 # Nakreslí tabulku    
    for j in range(a):              # Nakreslí řádek        
        for i in range(4):          # Nakreslí čtverec
            forward(strana)
            right(90)
        forward(strana)
    left(180)
    forward(a*strana)
    left(90)
    forward(strana)
    left(90)
penup()                             # Zvednutí tužky, přerušení psaní

c=(ceil((a*b)/2))                   # Maximální počet tahů
p=0                                 # Počítadlo tahů

for l in range(c):                  # Nakreslí křížky a kolečka
    print("Na tahu je první hráč")
    x=int(input("Sloupec: "))       # První hráč zadá číslo sloupce, do kterého chce nakreslit křížek
    while x>a or x<=0:              # Číslo nesmí být vyšší, než je počet sloupců a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        x=int(input("Sloupec: "))
    
    y=int(input("Řádek: "))         # První hráč zadá číslo řádku, do kterého chce nakreslit křížek
    while y>b or y<=0:              # Číslo nesmí být vyšší, než je počet řádků a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        y=int(input("Řádek: "))

    setpos(x*50-25, -y*50+25)       # Souřadnice políčka v mřížce
    pendown()                       # Položení tužky, pokračování ve psaní
    for m in range(4):              # Nakreslení křížku
        left(45)
        forward(20)
        left(180)
        forward(20)
        left(45)
    penup()

    p=p+1                           # Přičtení tahu
    if p==a*b:                      # Pokud se počet tahů rovná počtu polí, hra skončí
        break

    print("Na tahu je druhý hráč")
    x=int(input("Sloupec: "))       # Druhý hráč zadá číslo sloupce, do kterého chce nakreslit kolečko
    while x>a or x<=0:              # Číslo nesmí být vyšší, než je počet sloupců a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        x=int(input("Sloupec: "))

    y=int(input("Řádek: "))         # Druhý hráč zadá číslo řádku, do kterého chce nakreslit kolečko
    while y>b or y<=0:              # Číslo nesmí být vyšší, než je počet řádků a zároveň nesmí být nižší nebo rovné nule
        print("Zkus to znovu")
        y=int(input("Řádek: "))

    setpos(x*50-25, -y*50+25-20)    # Nakreslení kolečka
    pendown()
    circle(20)
    penup()
    
    p=p+1                           # Přičtení tahu
    if p==a*b:
        break

print("Pěkná hra!")

exitonclick()                       # Okno se samo nezavře