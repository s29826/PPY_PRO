from enum import Enum

#Nie wiem, czy ten Enum ma tutaj sens, do przemyślenia
class Obecnosc(Enum):
    Nieobecny = 0
    Spozniony = 1
    Obecny = 2
    Usprawiedliwiony = 3

    @staticmethod
    def ze_skrotu(skrot : str):
        match skrot.lower():
            case 'o':
                return Obecnosc.Obecny
            case 'n':
                return Obecnosc.Nieobecny
            case "u":
                return Obecnosc.Usprawiedliwiony
            case "s":
                return Obecnosc.Spozniony
        return None
