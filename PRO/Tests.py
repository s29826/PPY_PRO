from Uczen import Uczen
from Klasa import Klasa

#TEST1
def dodaj_dane_testowe():
    klasa1 = Klasa("1a")
    klasa1.dodaj_ucznia(Uczen("Kryspin", "Kroske", "30345"))
    klasa1.dodaj_ucznia(Uczen("Tristan", "Troske", "30543"))
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

