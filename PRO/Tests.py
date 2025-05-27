import random

from Obecnosc import Obecnosc
from Ocena import Ocena
from Uczen import Uczen
from Klasa import Klasa

#TEST1
def generuj_pesel() -> str:
    dziesiec_pierwszych : str = ""
    rok = random.randint(0, 99)
    if rok < 10:
        dziesiec_pierwszych = '0'
    dziesiec_pierwszych += str(rok)

    msc = random.randint(1, 24)
    norm_mnth = msc
    if msc > 12:
        norm_mnth = msc - 12
        msc = msc + 8 # -12 (żeby był poprawny indeks miesiąca) + 20 (bo taka jest konwencja różnych tysiącleci)
    if msc < 10:
        dziesiec_pierwszych += '0'

    dziesiec_pierwszych += str(msc)

    dni_miesiecy = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dzien = random.randint(1, dni_miesiecy[norm_mnth - 1])
    if dzien < 10:
        dziesiec_pierwszych += '0'

    dziesiec_pierwszych += str(dzien)

    uid = str(random.randint(0, 9999))
    uid = '0' * (4 - len(uid)) + uid
    dziesiec_pierwszych += uid

    wagi = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 0)
    kontrola = 0
    for idx, cyfra in enumerate(dziesiec_pierwszych):
        kontrola += int(cyfra) * wagi[idx]

    kontrola = (10 - (kontrola % 10)) % 10
    return dziesiec_pierwszych + str(kontrola)

def dodaj_dane_testowe():
    klasa1 = Klasa("1a")
    uczen1 = Uczen("Kryspin", "Kroske", generuj_pesel())
    uczen2 = Uczen("Tristan", "Troske", generuj_pesel())
    klasa1.dodaj_ucznia(uczen1)
    klasa1.dodaj_ucznia(uczen2)
    klasa1.dodaj_ucznia(Uczen("Krystyna", "Kluska", generuj_pesel()))
    klasa1.dodaj_ucznia(Uczen("Kirsten", "Kloskson", generuj_pesel()))
    klasa1.dodaj_ucznia(Uczen("Christian", "Closekey", generuj_pesel()))
    klasa2 = Klasa("1b")
    klasa3 = Klasa("2a")
    klasa4 = Klasa("3a")
    Klasa.lista_klas().append(klasa1)
    Klasa.lista_klas().append(klasa2)
    Klasa.lista_klas().append(klasa3)
    Klasa.lista_klas().append(klasa4)

    uczen1.dodaj_obecnosc("2025/05/25", Obecnosc.Obecny)
    uczen1.dodaj_obecnosc("2025/05/26", Obecnosc.Obecny)
    uczen1.dodaj_obecnosc("2025/05/27", Obecnosc.Nieobecny)
    uczen1.dodaj_obecnosc("2025/05/28", Obecnosc.Usprawiedliwiony)
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.0, "2025-05-25"))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.5, "2025-05-24"))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.5, "2025-05-23"))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 5.0, "2025-05-22"))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 2.0, "2025-05-22"))

    uczen2.dodaj_ocene(Ocena("Sprawdzian", 5.0, "2025-05-22"))
    uczen2.dodaj_ocene(Ocena("Sprawdzian", 4.0, "2025-05-22"))
    uczen2.dodaj_ocene(Ocena("Sprawdzian", 4.0, "2025-05-22"))
