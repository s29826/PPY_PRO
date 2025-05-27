from datetime import date


class Ocena():
    def __init__(self, rodzaj: str, ocena: float, data: date):
        self.rodzaj = rodzaj
        self.ocena = ocena
        self.data = data

    def __str__(self):
        return f"Komentarz: {self.rodzaj}, Ocena: {self.ocena}, Data: {self.data}"

    @staticmethod
    def walidacja(string : str) -> bool:
        try:
            liczba = float(string)
        except ValueError:
            return False

        return 1 <= liczba <= 5 and ((liczba * 2) - int(liczba * 2)) < 0.01
