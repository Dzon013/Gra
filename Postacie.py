import pygame
from Inne import Zycie
from Inne import Oslona
from Inne import Obrazenia


class Bohater:
    def __init__(self, x, y, grafika, hp, obrazenia, oslona):
        self.x = x
        self.y = y
        self.grafika = pygame.image.load(grafika)
        self.wysokosc = self.grafika.get_height()
        self.szerokosc = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc = 10
        self.hp = hp
        self.obrazenia = obrazenia
        self.oslona = oslona

    def tick(self, up, down, left, right):
        klawisze = pygame.key.get_pressed()
        if klawisze[up]:
            self.y -= self.predkosc
        if klawisze[down]:
            self.y += self.predkosc
        if klawisze[left]:
            self.x -= self.predkosc
        if klawisze[right]:
            self.x += self.predkosc

        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    def draw(self, okno):
        okno.blit(self.grafika, (self.x, self.y))

        zycie_bohater1 = Zycie(self.hp, self.obrazenia)
        zycie_bohater2 = Zycie(self.hp, self.obrazenia)
        zycie_bohater3 = Zycie(self.hp, self.obrazenia)

        oslona_bohater1 = Oslona(self.oslona, self.obrazenia)
        oslona_bohater2 = Oslona(self.oslona, self.obrazenia)
        oslona_bohater3 = Oslona(self.oslona, self.obrazenia)

        zycie_bohater1.draw(okno, 5, 600, 30, 300)
        zycie_bohater2.draw(okno, 5, 600, 30, 300)
        zycie_bohater3.draw(okno, 5, 600, 30, 300)

        oslona_bohater1.draw(okno, 5, 500, 30, 300)
        oslona_bohater2.draw(okno, 5, 500, 30, 300)
        oslona_bohater3.draw(okno, 5, 500, 30, 300)

        obrazenia_bohater1 = Obrazenia(self.obrazenia)
        obrazenia_bohater2 = Obrazenia(self.obrazenia)
        obrazenia_bohater3 = Obrazenia(self.obrazenia)

        obrazenia_bohater1.draw(okno, 5, 400, 30, 300)
        obrazenia_bohater2.draw(okno, 5, 400, 30, 300)
        obrazenia_bohater3.draw(okno, 5, 400, 30, 300)


class Przeciwnik:
    def __init__(self, x, y, grafika, hp, oslona, obrazenie):
        # self.imie = imie
        self.x = x
        self.y = y
        self.grafika = pygame.image.load(grafika)
        self.wysokosc = self.grafika.get_height()
        self.szerokosc = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc = 10
        self.hp = hp
        self.obrazenie = obrazenie
        self.oslona = oslona

    def tick(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    def draw(self, okno):
        okno.blit(self.grafika, (self.x, self.y))
        zycie_przeciwnik = Zycie(self.hp)
        zycie_przeciwnik.draw(okno, 500, 0, 20, 300)
        oslona_przeciwnik = Oslona(self.oslona, self.obrazenie)
        oslona_przeciwnik.draw(okno, 400, 0, 20, 300)
        obrazenia_przeciwnik = Obrazenia(self.obrazenie)
        obrazenia_przeciwnik.draw(okno, 300, 0, 20, 300)
