import datetime

from matplotlib import pyplot as plt

from Ocena import Ocena
from Uczen import Uczen

class Klasa:
    klasy : list = []

    def __init__(self, nazwa : str):
        self.nazwa : str = nazwa
        self.uczniowie = dict()

    @staticmethod
    def lista_klas():
        return Klasa.klasy

    def dodaj_ucznia(self, uczen : Uczen) -> None:
        self.uczniowie[uczen.pesel] = uczen

    def usun_ucznia(self, pesel : str) -> None:
        del self.uczniowie[pesel]

    def edytuj_ucznia(self, uczen : Uczen) -> None:
        del self.uczniowie[uczen.pesel]
        self.dodaj_ucznia(uczen)

    def wystaw_ocene(self, pesel : str, komentarz : str, ocena : float, data : datetime) -> None:
        self.uczniowie[pesel].dodaj_ocene(Ocena(komentarz, ocena, data))

    def wygeneruj_wykres_srednich(self) -> None:
        dane = {
            uczen.krotki_string() : uczen.oblicz_srednia()
            for uczen in self.uczniowie.values()
            if uczen.oceny
        }

        dane_sorted = sorted(dane.items(), key=lambda x : x[1], reverse=True)

        uczniowe = [uczen for uczen, srednia in dane_sorted]
        srednie = [srednia for uczen, srednia in dane_sorted]

        plt.bar(uczniowe, srednie, color='red')
        plt.ylabel("Średnia ocen")
        plt.title(f"Średnia ocen w klasie {self.nazwa}")
        plt.tight_layout()
        plt.show()

