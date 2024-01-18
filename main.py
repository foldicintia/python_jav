import szin
import oszthato
import autom


szin.szin_bekeres()

szamok=oszthato.szamok_lista()
print(szamok)

szamlalo=oszthato.hettelOszthato(szamok)
print(f"A héttel osztható számok száma: {szamlalo}")


kocsi=autom.beolvas()
print(f"{kocsi}")

autom.autok(kocsi)


db=autom.flotta(kocsi)
print(f"{db} db autó van a flottában")

max_index=autom.ertekes(kocsi)
print(f"A legöregebb autó: {kocsi[max_index].nev}. Gyártási éve: {kocsi[max_index].ev}")