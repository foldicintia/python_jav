"""Készítsen programot autom.py néven. Olvassa be auto.txt fájlból az auto adatait, 
tárolja Auto osztály típusú kocsi nevű listában a példányokat. 
Készítsen metódust:
•	kor néven, amely a paraméterként kapott autó márkáját és korát adja vissza a konzolra.
•	kiir metódust, amely kiírja ki.txt fájlba az autók márkáját és korát az alábbi formában.
Készíts függvényt:
•	flotta néven, amely kiírja hány autónk van.
•	ertekes néven, ami kiírja a legöregebb autó nevét, és gyártási dátumát.
"""
from Auto import Auto

def beolvas():
    kocsi=[]
    fajl=open("auto.txt","r",encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    for i in range(0,len(nyers_lista),1):
        sor=nyers_lista[i]
        elem=sor.strip().split(":")
        nev: str =elem[0]
        ev: int =elem[1]
        auto=Auto(nev,ev)
        kocsi.append(auto)
    return kocsi

def autok(kocsi):
    for i in range(0,len(kocsi),1):
      print(f"Az autó márkája: {kocsi[i].nev}, kora: {2024 - int(kocsi[i].ev)}")


def flotta(kocsi):
    db=len(kocsi)
    return db

def ertekes(kocsi):
    legoregebb_index = 0
    for i in range(0, len(kocsi),1):
        if kocsi[i].ev < kocsi[legoregebb_index].ev:
            legoregebb_index = i
    return legoregebb_index