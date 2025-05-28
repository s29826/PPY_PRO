import random
import datetime

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
    klasa2 = Klasa("1b")
    klasa3 = Klasa("2a")
    klasa4 = Klasa("3a")

    uczen1 = Uczen("Kryspin", "Kroske", generuj_pesel())
    uczen2 = Uczen("Krystyna", "Kluska", generuj_pesel())
    uczen3 = Uczen("Christian", "Closekey", generuj_pesel())
    uczen4 = Uczen("Krystianus", "Kloskus", generuj_pesel())
    uczen5 = Uczen("Tristan", "Troske", generuj_pesel())
    uczen6 = Uczen("Tristana", "Troska", generuj_pesel())
    uczen7 = Uczen("Kloskeusz", "Krystian", generuj_pesel())
    uczen8 = Uczen("Kryspin", "Kloski", generuj_pesel())
    uczen9 = Uczen("Chris", "Klos", generuj_pesel())
    uczen10 = Uczen("Krystian", "Kloskhaus", generuj_pesel())

    klasa1.dodaj_ucznia(uczen1)
    klasa1.dodaj_ucznia(uczen2)
    klasa1.dodaj_ucznia(uczen3)
    klasa1.dodaj_ucznia(uczen4)
    klasa2.dodaj_ucznia(uczen5)
    klasa2.dodaj_ucznia(uczen6)
    klasa2.dodaj_ucznia(uczen7)
    klasa2.dodaj_ucznia(uczen8)
    klasa3.dodaj_ucznia(uczen9)
    klasa3.dodaj_ucznia(uczen10)

    Klasa.lista_klas().append(klasa1)
    Klasa.lista_klas().append(klasa2)
    Klasa.lista_klas().append(klasa3)
    Klasa.lista_klas().append(klasa4)

    uczen1.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-25"), Obecnosc.Obecny)
    uczen1.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-26"), Obecnosc.Obecny)
    uczen1.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-27"), Obecnosc.Nieobecny)
    uczen1.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-28"), Obecnosc.Usprawiedliwiony)
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.0, datetime.datetime.fromisoformat("2025-05-25")))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.5, datetime.datetime.fromisoformat("2025-05-26")))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 3.5, datetime.datetime.fromisoformat("2025-05-27")))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 5.0, datetime.datetime.fromisoformat("2025-05-28")))
    uczen1.dodaj_ocene(Ocena("Sprawdzian", 2.0, datetime.datetime.fromisoformat("2025-05-29")))

    uczen2.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-25"), Obecnosc.Obecny)
    uczen2.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-26"), Obecnosc.Obecny)
    uczen2.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-27"), Obecnosc.Obecny)
    uczen2.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-28"), Obecnosc.Nieobecny)
    uczen2.dodaj_ocene(Ocena("Sprawdzian", 5.0, datetime.datetime.fromisoformat("2025-05-25")))
    uczen2.dodaj_ocene(Ocena("Kolokwium", 4.5, datetime.datetime.fromisoformat("2025-05-26")))
    uczen2.dodaj_ocene(Ocena("Kolokwium", 3.5, datetime.datetime.fromisoformat("2025-05-27")))
    uczen2.dodaj_ocene(Ocena("Egzamin", 5.0, datetime.datetime.fromisoformat("2025-05-28")))
    uczen2.dodaj_ocene(Ocena("Kartkówka", 2.0, datetime.datetime.fromisoformat("2025-05-29")))

    uczen3.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-25"), Obecnosc.Nieobecny)
    uczen3.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-26"), Obecnosc.Usprawiedliwiony)
    uczen3.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-27"), Obecnosc.Nieobecny)
    uczen3.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-28"), Obecnosc.Obecny)

    uczen3.dodaj_ocene(Ocena("Sprawdzian", 5.0, datetime.datetime.fromisoformat("2025-05-26")))
    uczen3.dodaj_ocene(Ocena("Sprawdzian", 5.0, datetime.datetime.fromisoformat("2025-05-27")))
    uczen3.dodaj_ocene(Ocena("Sprawdzian", 4.0, datetime.datetime.fromisoformat("2025-05-28")))
    uczen3.dodaj_ocene(Ocena("Kartkówka", 4.5, datetime.datetime.fromisoformat("2025-05-29")))
    uczen3.dodaj_ocene(Ocena("Wejściówka", 4.0, datetime.datetime.fromisoformat("2025-05-30")))

    uczen4.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-25"), Obecnosc.Obecny)
    uczen4.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-26"), Obecnosc.Obecny)
    uczen4.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-27"), Obecnosc.Obecny)
    uczen4.dodaj_obecnosc(datetime.datetime.fromisoformat("2025-05-28"), Obecnosc.Usprawiedliwiony)
    uczen4.dodaj_ocene(Ocena("Sprawdzian", 2.0, datetime.datetime.fromisoformat("2025-05-25")))
    uczen4.dodaj_ocene(Ocena("Kartkówka", 2.5, datetime.datetime.fromisoformat("2025-05-26")))
    uczen4.dodaj_ocene(Ocena("Sprawdzian", 2.5, datetime.datetime.fromisoformat("2025-05-27")))
    uczen4.dodaj_ocene(Ocena("Sprawdzian", 3.0, datetime.datetime.fromisoformat("2025-05-28")))
    uczen4.dodaj_ocene(Ocena("Wejściówka", 3.0, datetime.datetime.fromisoformat("2025-05-29")))
