import pygame
from Przyciski import Przyciski
from Postacie import Bohater
from Postacie import Przeciwnik
from Belki import Belki


pygame.init()
okno = pygame.display.set_mode((1291, 720))


def mapa(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    tlo = pygame.image.load("Zdjęcia/tla/mapa.png")
    tlo2 = pygame.image.load("Zdjęcia/tla/dialog.png")
    teksty = {"Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "dialog1": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do lasu ?", True, (255, 255, 255)),
              "dialog2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do jaskini ?", True, (255, 255, 255)),
              "dialog3": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do miasta ?", True, (255, 255, 255)),
              "dialog4": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie na cmentarz ?", True, (255, 255, 255))
              }
    przyciski = {
        "wyjdz": Przyciski(500, 500, "Wyjdź"),
        "tak": Przyciski(900, 600, "tak")
    }
    belki = {
        "granica1": Belki(0, -10, 820, 10, (0, 0, 0)),
        "granica2": Belki(1, 1, 10, 1291, (0, 0, 0)),
        "granica3": Belki(1281, -10, 1291, 10, (0, 0, 0)),
        "granica4": Belki(0, 710, 10, 1291, (0, 0, 0)),
        "wioska": Belki(690, 620, 50, 50, (255, 0, 100)),
        "las": Belki(80, 520, 50, 50, (255, 200, 100)),
        "jaskinia": Belki(950, 530, 50, 50, (55, 60, 100)),
        "miasto": Belki(410, 211, 50, 50, (5, 100, 60)),
        "boss": Belki(345, 460, 50, 50, (0, 0, 0)),
        "zbrojownia": Belki(135, 108, 50, 50, (0, 0, 0)),
        "cmentarz": Belki(730, 125, 50, 50, (0, 0, 0)),
        "drugi_swiat": Belki(1100, 180, 50, 50, (0, 0, 0)),
    }
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
    bohater1 = Bohater(735, 311, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(735, 311, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(735, 311, postacie["postac3"], 100, 10, 1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        belki["granica1"].draw(okno)
        belki["granica2"].draw(okno)
        belki["granica3"].draw(okno)
        belki["granica4"].draw(okno)
        belki["wioska"].draw(okno)
        belki["miasto"].draw(okno)
        belki["las"].draw(okno)
        belki["jaskinia"].draw(okno)
        belki["cmentarz"].draw(okno)
        belki["boss"].draw(okno)
        belki["zbrojownia"].draw(okno)
        belki["drugi_swiat"].draw(okno)

        okno.blit(tlo, (0, 0))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        bohater1.tick(strzalki["up"], strzalki["down"], strzalki["left"], strzalki["right"])
        bohater2.tick(wsad["w"], wsad["s"], wsad["a"], wsad["d"])
        bohater3.tick(ikjl["5"], ikjl["2"], ikjl["1"], ikjl["3"])

        if bohater1.hitbox.colliderect(belki["wioska"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                miasto(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater1.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater1.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater1.hitbox.colliderect(belki["boss"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["zbrojownia"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater1.hitbox.colliderect(belki["granica1"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["granica2"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["granica3"].hitbox):
            pass
        if bohater1.hitbox.colliderect(belki["granica4"].hitbox):
            pass

        if bohater2.hitbox.colliderect(belki["wioska"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                miasto(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater2.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater2.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater2.hitbox.colliderect(belki["boss"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["zbrojownia"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater2.hitbox.colliderect(belki["granica1"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["granica2"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["granica3"].hitbox):
            pass
        if bohater2.hitbox.colliderect(belki["granica4"].hitbox):
            pass

        if bohater3.hitbox.colliderect(belki["wioska"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():miasto(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater3.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater3.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater3.hitbox.colliderect(belki["boss"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["zbrojownia"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3)

        if bohater3.hitbox.colliderect(belki["granica1"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["granica2"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["granica3"].hitbox):
            pass
        if bohater3.hitbox.colliderect(belki["granica4"].hitbox):
            pass

        pygame.display.update()


def las(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    teksty = {"Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255))
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Zdjęcia/Bohater.png",
                "postac2": "Zdjęcia/Bohater/stand.png",
                "postac3": "Zdjęcia/Bohater3.png"}

    przeciwnik = {"przeciwnik": "Zdjęcia/goblin.png"}
    
    bohater1 = Bohater(375, 540, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(375, 540, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(375, 540, postacie["postac3"], 100, 10, 1)

    przeciwnik = Przeciwnik(800, 540, przeciwnik["przeciwnik"], 50, 10, 5)

    tlo = pygame.image.load("Zdjęcia/tla/las.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                pauza = not pauza

        okno.blit(tlo, (0, 0))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def cmentarz(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    teksty = {"Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255))
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}
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
    bohater1 = Bohater(375, 540, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(375, 540, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(375, 540, postacie["postac3"], 100, 10, 1)

    tlo = pygame.image.load("Zdjęcia/tla/cmentarz.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                pauza = not pauza

        okno.blit(tlo, (0, 0))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def jaskinia(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    teksty = {"Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255))
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}
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
    bohater1 = Bohater(375, 540, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(375, 540, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(375, 540, postacie["postac3"], 100, 10, 1)

    tlo = pygame.image.load("Zdjęcia/tla/jaskinia.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.type == pygame.K_ESCAPE:
                pauza = not pauza

        okno.blit(tlo, (0, 0))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def miasto(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    teksty = {"Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}
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
    bohater1 = Bohater(375, 540, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(375, 540, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(375, 540, postacie["postac3"], 100, 10, 1)

    tlo = pygame.image.load("Zdjęcia/tla/miasto.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                pauza = not pauza

        okno.blit(tlo, (0, 0))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def lobby(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    teksty = {"Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255))
              }
    sterowanie = {"WSAD": pygame.image.load("Zdjęcia/sterowanie1.png"),
                  "GLDP": pygame.image.load("Zdjęcia/sterowanie2.png"),
                  "IKJL": pygame.image.load("Zdjęcia/sterowanie3.png")
                  }
    postacie = {"postac1": "Zdjęcia/Bohater.png",
                "postac2": "Zdjęcia/Bohater/stand.png",
                "postac3": "Zdjęcia/Bohater3.png"}
    bohater1 = Bohater(500, 500, postacie["postac1"], 100, 10, 1)
    bohater2 = Bohater(500, 500, postacie["postac2"], 100, 10, 1)
    bohater3 = Bohater(500, 500, postacie["postac3"], 100, 10, 1)

    przyciski = {"Graj": Przyciski(1000, 400, "Przycisk"),
                 "Wyjdź": Przyciski(1000, 500, "Wyjdź"),
                 "Postac1": Przyciski(100, 0, "Postac1"),
                 "Postac2": Przyciski(300, 0, "Postac2"),
                 "Postac3": Przyciski(500, 0, "Postac3"),
                 "Multiplayer": Przyciski(1000, 600, "Multiplayer")
                 }

    tlo = pygame.image.load("Zdjęcia/tla/Lobby.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if przyciski["Graj"].tick():
            mapa(draw_bohater1, draw_bohater2, draw_bohater3)
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
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(sterowanie["WSAD"], (1000, 0))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(sterowanie["GLDP"], (1000, 0))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
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
    przyciski = {
        "Graj": Przyciski(550, 444, "Przycisk"),
        "Wyjdz": Przyciski(550, 550, "Wyjdź")
    }
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if przyciski["Graj"].tick():
            run = True
            lobby(draw_bohater1=False, draw_bohater2=False, draw_bohater3=False)

        if przyciski["Wyjdz"].tick():
            run = False

        okno.blit(pygame.image.load("Zdjęcia/tla/tło początkowe.png"), (0, 0))
        przyciski["Graj"].draw(okno)
        przyciski["Wyjdz"].draw(okno)
        pygame.display.update()


if __name__ == '__main__':
    main()
