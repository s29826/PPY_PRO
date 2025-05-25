from datetime import date


class Ocena():
    def __init__(self, rodzaj: str, ocena: float, data: date):
        self.rodzaj = rodzaj
        self.ocena = ocena
        self.data = data

    def __str__(self):
        return f"Komentarz: {self.rodzaj}, Ocena: {self.ocena}, Data: {self.data}"
