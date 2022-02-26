class Fraction:

    def __init__(self, nom: int = 0, denom: int = 1) -> None:
        self.nom = nom
        self.denom = denom

    def vvod(self) -> None:
        self.nom = int(input('Введите числитель>> '))
        self.denom = int(input('Введите знаменатель>> '))
        if self.denom == 0:
            raise ZeroDivisionError

    def __str__(self) -> str:
        return f"{self.ch}/{self.zn}"


a1 = Fraction()
print(a1)
