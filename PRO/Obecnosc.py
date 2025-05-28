from enum import Enum

class Obecnosc(Enum):
    Nieobecny = 0
    Spozniony = 1
    Obecny = 2
    Usprawiedliwiony = 3

    @staticmethod
    def ze_skrotu(skrot : str) -> 'Obecnosc':
        match skrot.lower():
            case 'o':
                return Obecnosc.Obecny
            case 'n':
                return Obecnosc.Nieobecny
            case "u":
                return Obecnosc.Usprawiedliwiony
            case "s":
                return Obecnosc.Spozniony
        raise TypeError
