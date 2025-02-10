import pygame


class Belki:
    def __init__(self, x, y, wysokosc, szerokosc, kolor):
        self.x = x
        self.y = y
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.hitbox = self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.kolor = kolor

    def draw(self, okno):
        pygame.draw.rect(okno, self.kolor, self.hitbox)
