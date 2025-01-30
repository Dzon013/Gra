import pygame


class Bohater:
    def __init__(self, x, y, grafika):
        # self.imie = imie
        self.x = x
        self.y = y
        self.grafika = pygame.image.load(grafika)
        self.wysokosc = self.grafika.get_height()
        self.szerokosc = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc = 10

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

    def draw(self, okno):
        okno.blit(self.grafika, (self.x, self.y))
