"""
Írjon modult szin.py néven! A program kérjen be egy szín keverési módszert szövegként. 
    pl.: RGB, HEX, HSL, RGBA, HSLA …stb. Majd olvassa be a hozzá tartozó színkódot szintén szövegként. 
Ha a felhasználó HEX kulcsszót adott meg akkor 6 hosszúnak kel lennie a kódnak. Ha a felhasználó RGB akkor 5-11 karakterű lehet a kód, 
ha vagy HSL kódot adott meg akkor 7-13 karakterű lehet a kód. Írd ki a felhasználónak a mintában szereplő kódokat, 
hogy megfelelnek-e hossz alapján a feltételeknek. A többi módszernél írja ki a program, hogy bonyolult kiszámolni.
A program üzeneteinek megfogalmazásában kövesse az alábbi példát! Azokat a részeket, amiket a felhasználó gépel be, a mintában vastagított 
és döntött betűkkel emeltük ki. 
"""

def szin_bekeres():
    szin: str = input("Adjon meg egy színkeverési módszert!:")
    kod: int = input("Adja meg a színkódot!:")
    if szin == "RGB":
        if not (len(kod) > 4 and len(kod) < 12):
            print("Nem megfelelő a kód hossza.")
        else:
            print("Megfelelő hossz")
    elif szin == "HSL":
        if len(kod) < 14 and len(kod) > 6:
            print("Megfelelő hossz")
        else:
            print("Nem megfelelő a kód hossza")
    else:
        print("Bonyolult kiszámolni")