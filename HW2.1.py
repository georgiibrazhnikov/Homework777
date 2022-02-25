class Fraction:

    def __init__(self, nom: int = 1, denom: int = 0):
        self.nom = nom
        self.denom = denom

    def vvod(self):
        self.nom = int(input('Введите числитель>> '))
        self.denom = int(input('Введите знаменатель>> '))
        if self.denom == 0:
            print('Знаменатель не должен равняться нулю.')

    def __str__(self):
        return f"{self.ch}/{self.zn}"
