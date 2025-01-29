import pygame
from Przyciski import Przyciski
from Postacie import Bohater
from Postacie import Bohater2

pygame.init()
okno = pygame.display.set_mode((1200, 886))


def pierwszy_swiat():
    run = True
    bohater = Bohater(0, 0) or Bohater2(0, 0)
    zegar = 0
    tlo = pygame.image.load("Zdjęcia/las.png")
    while run:
        zegar += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        bohater.tick()

        okno.blit(tlo, (0, 0))
        bohater.draw(okno)
        pygame.display.update()


def lobby():
    run = True
    bohater1 = Bohater(500, 500)
    bohater2 = Bohater2(500, 500)
    przyciski = [Przyciski(1000, 600, "Przycisk"),
                 Przyciski(1000, 700, "Wyjdź"),
                 Przyciski(100, 0, "Postac1"),
                 Przyciski(300, 0, "Postac2"),
                 Przyciski(500, 0, "Postac3"),
                 Przyciski(1000, 500, "Multiplayer")
                 ]
    tlo = pygame.image.load("Zdjęcia/Lobby.png")
    draw_bohater1 = False
    draw_bohater2 = False

    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        if przyciski[0].tick():
            pierwszy_swiat()
        if przyciski[1].tick():
            run = False

        bohater1.tick()
        bohater2.tick()

        okno.blit(tlo, (0, 0))
        przyciski[0].draw(okno)
        przyciski[1].draw(okno)
        przyciski[2].draw(okno)
        przyciski[3].draw(okno)
        przyciski[4].draw(okno)
        przyciski[5].draw(okno)
        if draw_bohater1 is True:
            bohater1.draw(okno)

        if draw_bohater2 is True:
            bohater2.draw(okno)

        if przyciski[2].tick():
            draw_bohater1 = True
            draw_bohater2 = False

        if przyciski[3].tick():
            draw_bohater1 = False
            draw_bohater2 = True

        pygame.display.update()


def main():
    run = True
    przyciski = [
        Przyciski(550, 444, "Przycisk"),
        Przyciski(550, 550, "Wyjdź")
    ]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if przyciski[0].tick():
            run = True
            lobby()

        if przyciski[1].tick():
            run = False

        okno.blit(pygame.image.load("Zdjęcia/tło początkowe.png"), (0, 0))
        przyciski[0].draw(okno)
        przyciski[1].draw(okno)
        pygame.display.update()


if __name__ == '__main__':
    main()
