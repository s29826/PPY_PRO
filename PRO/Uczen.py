from Obecnosc import Obecnosc
from Ocena import Ocena
from datetime import date


class Uczen:
    def __init__(self, imie: str, nazwisko: str, pesel: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.oceny = list()
        #Zakładam, że uczeń będzie miał sprawdzaną listę raz dziennie
        self.obecnosci = dict()
        self.zagrozenie = False

    def dodaj_obecnosc(self, data: date, obecnosc: Obecnosc) -> None:
        self.obecnosci[data] = obecnosc

    def dodaj_ocene(self, ocena: Ocena) -> None:
        self.oceny.append(ocena)

    def oblicz_srednia(self) -> float:
        suma_ocen = 0

        for ocena in self.oceny:
            suma_ocen += ocena.ocena

        return suma_ocen / len(self.oceny)

    def __str__(self):
        return (f"Imię: {self.imie}, Nazwisko: {self.nazwisko}"
                f", Obecność: {self.obecnosci}, Zagrożenie: {self.zagrozenie}")
