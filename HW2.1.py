from math import *

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
        return f"{self.nom}/{self.denom}"

    def reduse(self) -> str:
        if self.nom == 0:
            return
        z = gcd(self.nom, self.denom)
        self.nom = self.nom // z
        self.denom = self.denom // z
       
   
class IrreduceableFraction(Fraction):
    def __init__(self, *args, *kwargs):
        super().__init__(*args, *kwargs)
     def vvod(self, *args, *kwargs)
        super().vvod(*args, *kwargs)
        self.reduse()

        
a1 = Fraction()
print(a1)


f1 = IrreduceableFraction(4, 2)
b1 = IrreduceableFraction(10, 5)

asert f1 == b1
