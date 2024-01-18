"""
A program egy listát vizsgál. Egy függvény segítségével megszámolja, hogy a listában hány darab héttel osztható szám található. 
Írjon modult oszthato.py néven!  
Írja meg azt a hettelOszthato nevű függvényt, amely megszámolja egy adott listában hány darab héttel osztható szám van! 
A függvény paramétere lista legyen, a visszatérési értéke a listában szereplő héttel osztható számok darabszáma legyen! 
Hozzon létre egy szamok listát, melyet töltsön fel 50 darab 1 és 100 közé eső véletlen számokkal! Írja ki a lista elemeit! 
Hívja meg a programban a megírt függvényt és írja ki, hogy hány darab héttel osztható szám van a listában!
"""
import random

def hettelOszthato(szamok):

    for i in range(0,50,1):
        szam = random.randint(1,100)
        szamok.append(szam)
    print(szamok)
