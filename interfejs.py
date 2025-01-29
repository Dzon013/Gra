import pygame
from Przyciski import Przyciski
from Postacie import Bohater

pygame.init()
okno = pygame.display.set_mode((1291, 720))


def mapa():
    pass


def pierwszy_swiat():
    run = True

    strzalki = {"up": pygame.K_UP,
                "down": pygame.K_DOWN,
                "left": pygame.K_LEFT,
                "right": pygame.K_RIGHT}
    wsad = {"w": pygame.K_w,
            "s": pygame.K_s,
            "a": pygame.K_a,
            "d": pygame.K_d}
    ikjl = {"5": pygame.K_i,
            "2": pygame.K_k,
            "1": pygame.K_j,
            "3": pygame.K_l}

    postacie = {"postac1": "Zdjęcia/Bohater.png",
                "postac2": "Zdjęcia/Bohater/stand.png",
                "postac3": "Zdjęcia/Bohater3.png"}
    bohater1 = Bohater(500, 500, postacie["postac1"])
    bohater2 = Bohater(500, 500, postacie["postac2"])
    bohater3 = Bohater(500, 500, postacie["postac3"])

    tlo = pygame.image.load("Zdjęcia/las.png")

    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        bohater1.tick(strzalki["up"], strzalki["down"], strzalki["left"], strzalki["right"])
        bohater2.tick(wsad["w"], wsad["s"], wsad["a"], wsad["d"])
        bohater3.tick(ikjl["5"], ikjl["2"], ikjl["1"], ikjl["3"])
        okno.blit(tlo, (0, 0))
        bohater1.draw(okno)
        pygame.display.update()


def lobby():
    run = True
    sterowanie = {"WSAD": pygame.image.load("Zdjęcia/sterowanie1.png"),
                  "GLDP": pygame.image.load("Zdjęcia/sterowanie2.png"),
                  "IKJL": pygame.image.load("Zdjęcia/sterowanie3.png")
                  }
    postacie = {"postac1": "Zdjęcia/Bohater.png",
                "postac2": "Zdjęcia/Bohater/stand.png",
                "postac3": "Zdjęcia/Bohater3.png"}
    bohater1 = Bohater(500, 500, postacie["postac1"])
    bohater2 = Bohater(500, 500, postacie["postac2"])
    bohater3 = Bohater(500, 500, postacie["postac3"])

    przyciski = {"Graj": Przyciski(1000, 600, "Przycisk"),
                 "Wyjdź": Przyciski(1000, 700, "Wyjdź"),
                 "Postac1": Przyciski(100, 0, "Postac1"),
                 "Postac2": Przyciski(300, 0, "Postac2"),
                 "Postac3": Przyciski(500, 0, "Postac3"),
                 "Multiplayer": Przyciski(1000, 500, "Multiplayer")
                 }

    tlo = pygame.image.load("Zdjęcia/Lobby.png")

    draw_bohater1 = False
    draw_bohater2 = False
    draw_bohater3 = False

    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        if przyciski["Graj"].tick():
            pierwszy_swiat()
        if przyciski["Wyjdź"].tick():
            run = False

        okno.blit(tlo, (0, 0))
        przyciski["Graj"].draw(okno)
        przyciski["Wyjdź"].draw(okno)
        przyciski["Postac1"].draw(okno)
        przyciski["Postac2"].draw(okno)
        przyciski["Postac3"].draw(okno)
        przyciski["Multiplayer"].draw(okno)

        if draw_bohater1 is True:
            bohater1.draw(okno)
            okno.blit(sterowanie["WSAD"], (1000, 0))

        if draw_bohater2 is True:
            bohater2.draw(okno)
            okno.blit(sterowanie["GLDP"], (1000, 0))

        if draw_bohater3 is True:
            bohater3.draw(okno)
            okno.blit(sterowanie["IKJL"], (1000, 0))

        if przyciski["Postac1"].tick():
            draw_bohater1 = True
            draw_bohater2 = False
            draw_bohater3 = False

        if przyciski["Postac2"].tick():
            draw_bohater1 = False
            draw_bohater2 = True
            draw_bohater3 = False

        if przyciski["Postac3"].tick():
            draw_bohater1 = False
            draw_bohater2 = False
            draw_bohater3 = True

        pygame.display.update()


def main():
    run = True
    zegar = 0
    przyciski = [
        Przyciski(550, 444, "Przycisk"),
        Przyciski(550, 550, "Wyjdź")
    ]
    while run:
        zegar += pygame.time.Clock().tick(60) / 1000
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
