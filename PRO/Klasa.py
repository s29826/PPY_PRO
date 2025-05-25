import datetime

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

