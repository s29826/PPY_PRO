from Obecnosc import Obecnosc
from Ocena import Ocena
from Uczen import Uczen
from Klasa import Klasa

#TEST1
def dodaj_dane_testowe():
    klasa1 = Klasa("1a")
    uczen1 = Uczen("Kryspin", "Kroske", "30345")
    uczen2 = Uczen("Tristan", "Troske", "30543")
    klasa1.dodaj_ucznia(uczen1)
    klasa1.dodaj_ucznia(uczen2)
    klasa1.dodaj_ucznia(Uczen("Krystyna", "Kluska", "50353"))
    klasa1.dodaj_ucznia(Uczen("Kirsten", "Kloskson", "05435"))
    klasa1.dodaj_ucznia(Uczen("Christian", "Closekey", "35540"))
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
