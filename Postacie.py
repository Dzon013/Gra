import pygame
from Inne import Zycie
from Inne import Oslona
from Inne import Obrazenia
from math import floor


class Bohater:
    def __init__(self, x, y, grafika, hp, obrazenia, oslona):
        self.x = x
        self.y = y
        self.stanie_prawo = pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/stanie.png")
        self.stanie_lewo = pygame.transform.flip(pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/stanie.png"), True, False)
        self.skok_prawo = pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/skok.png")
        self.skok_lewo = pygame.transform.flip(pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/skok.png"), True, False)
        self.chodzenie_prawo = [pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/Chodzenie/klatka0{x}.png") for x in range(1, 7)]
        self.chodzenie_lewo = [pygame.transform.flip(pygame.image.load(f"Zdjęcia/Bohaterowie/{grafika}/Chodzenie/klatka0{x}.png"), True, False) for x in range(1, 7)]
        self.wysokosc = self.stanie_prawo.get_height()
        self.szerokosc = self.stanie_prawo.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc_pion = 0
        self.predkosc_poziom = 0
        self.hp = hp
        self.obrazenia = obrazenia
        self.oslona = oslona
        self.wczesniejszy_x = x
        self.wczesniejszy_y = y
        self.ktora_klatka = 0
        self.kierunek = 0
        self.skakanie = False

    def tick(self, up, down, left, right):
        klawisze = pygame.key.get_pressed()
        if klawisze[up]:
            self.skakanie = True
            self.predkosc_pion = 10
            self.y -= self.predkosc_pion

        elif klawisze[down]:
            self.skakanie = True
            self.predkosc_pion = 10
            self.y += self.predkosc_pion

        elif klawisze[left]:
            self.skakanie = False
            self.kierunek = 1
            self.predkosc_poziom = 10
            self.x -= self.predkosc_poziom

        elif klawisze[right]:
            self.skakanie = False
            self.kierunek = 0
            self.predkosc_poziom = 10
            self.x += self.predkosc_poziom

        else:
            self.skakanie = False
            self.predkosc_poziom = 0
            self.predkosc_pion = 0

        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    def draw(self, okno):
        if self.skakanie:
            if self.kierunek == 0:
                okno.blit(self.skok_prawo, (self.x, self.y))
            elif self.kierunek == 1:
                okno.blit(self.skok_lewo, (self.x, self.y))

        elif self.predkosc_poziom != 0:
            if self.kierunek == 0:
                okno.blit(self.chodzenie_prawo[floor(self.ktora_klatka)], (self.x, self.y))
            if self.kierunek == 1:
                okno.blit(self.chodzenie_lewo[floor(self.ktora_klatka)], (self.x, self.y))
            self.ktora_klatka += 0.2
            if self.ktora_klatka > 5:
                self.ktora_klatka = 0

        else:
            if self.kierunek == 0:
                okno.blit(self.stanie_prawo, (self.x, self.y))
            if self.kierunek == 1:
                okno.blit(self.stanie_lewo, (self.x, self.y))

        zycie_bohater1 = Zycie(self.hp, self.obrazenia)
        zycie_bohater2 = Zycie(self.hp, self.obrazenia)
        zycie_bohater3 = Zycie(self.hp, self.obrazenia)

        zycie_bohater1.draw(okno, 5, 600, 30, 300)
        zycie_bohater2.draw(okno, 5, 600, 30, 300)
        zycie_bohater3.draw(okno, 5, 600, 30, 300)

        oslona_bohater1 = Oslona(self.oslona, self.obrazenia)
        oslona_bohater2 = Oslona(self.oslona, self.obrazenia)
        oslona_bohater3 = Oslona(self.oslona, self.obrazenia)

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
        zycie_przeciwnik = Zycie(self.hp, self.obrazenie)
        zycie_przeciwnik.draw(okno, 985, 600, 30, 300)
        oslona_przeciwnik = Oslona(self.oslona, self.obrazenie)
        oslona_przeciwnik.draw(okno, 985, 500, 30, 300)
        obrazenia_przeciwnik = Obrazenia(self.obrazenie)
        obrazenia_przeciwnik.draw(okno, 985, 400, 30, 300)
