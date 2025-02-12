import pygame


class Zycie:
    def __init__(self, max_zdrowie, obrazenia):
        self.max = max_zdrowie
        self.zdrowie = max_zdrowie
        self.obrazenie = obrazenia
        self.zyje = True

    def obrazenia(self):
        self.zdrowie -= self.obrazenie
        if self.zdrowie <= 0:
            self.zdrowie = 0
            self.zyje = not self.zyje

    def draw(self, okno, x, y, wysokosc, max_szerokosc):
        procent_szerokosci = self.zdrowie / self.max
        szerokosc = round(max_szerokosc * procent_szerokosci)
        pygame.draw.rect(okno, (30, 30, 30), (x, y, szerokosc, wysokosc))
        pygame.draw.rect(okno, (4, 252, 0), (x, y, max_szerokosc, wysokosc))


class Oslona:
    def __init__(self, max_oslona, obrazenie):
        self.max = max_oslona
        self.oslona = max_oslona
        self.obrazenie = obrazenie

    def obrazenia(self):
        self.oslona -= self.obrazenie
        if self.oslona <= 0:
            self.oslona = 0
            Zycie.obrazenia(self.obrazenie)

    def draw(self, okno, x, y, wysokosc, max_szerokosc):
        procent_szerokosci = self.oslona / self.max
        szerokosc = round(max_szerokosc * procent_szerokosci)
        pygame.draw.rect(okno, (30, 30, 30), (x, y, szerokosc, wysokosc))
        pygame.draw.rect(okno, (7, 222, 222), (x, y, max_szerokosc, wysokosc))


class Obrazenia:
    def __init__(self, obrazenie):
        self.obrazenie = obrazenie
        self.max = obrazenie

    def draw(self, okno, x, y, wysokosc, max_szerokosc):
        procent_szerokosci = self.obrazenie / self.max
        szerokosc = round(max_szerokosc * procent_szerokosci)
        pygame.draw.rect(okno, (30, 30, 30), (x, y, szerokosc, wysokosc))
        pygame.draw.rect(okno, (242, 0, 61), (x, y, max_szerokosc, wysokosc))
