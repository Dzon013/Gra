import pygame
from Przyciski import Przyciski
from Postacie import Bohater
from Postacie import Przeciwnik
from Belki import Belki

zdrowie = {"zdrowie1": 100,
           "zdrowie2": 150,
           "zdrowie3": 200}

obrazenia = {"demage1": 5,
             "demage2": 10,
             "demage3": 15}

oslona = {"oslona1": 1,
          "oslona2": 1,
          "oslona3": 1}

zdrowie_przeciwnik = {"zdrowie1": 50,
                      "zdrowie2": 100,
                      "zdrowie3": 150,
                      "zdrowie4": 250,
                      "zdrowie5": 1000}

obrazenia_przeciwnik = {"demage1": 5,
                        "demage2": 10,
                        "demage3": 15,
                        "demage4": 20,
                        "demage5": 50}

oslona_przeciwnik = {"oslona1": 1,
                     "oslona2": 5,
                     "oslona3": 10,
                     "oslona4": 15,
                     "oslona5": 100}

pygame.init()
okno = pygame.display.set_mode((1291, 720))


def mapa(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    pauza = False
    przeciwnicy = {"goblin": "Zdjęcia/goblin.png",
                   "pajak": "Zdjęcia/pajak.png",
                   "zniwiarz": "Zdjęcia/żniwiarz.png",
                   "terrorysci": "Zdjęcia/terroryści.png",
                   "boss": "Zdjęcia/smok.png"}

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
              "dialog4": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie na cmentarz ?", True, (255, 255, 255)),
              "dialog5": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do zbrojowni ?", True, (255, 255, 255)),
              "dialog6": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do bossa ?", True, (255, 255, 255)),
              "dialog7": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do wioski ?", True, (255, 255, 255)),
              "dialog8": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Czy chcesz udać sie do drugiego świata ?", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255))
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

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(735, 311, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(735, 311, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(735, 311, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])
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

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        if draw_bohater1:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        bohater1.tick(strzalki["up"], strzalki["down"], strzalki["left"], strzalki["right"])
        bohater2.tick(wsad["w"], wsad["s"], wsad["a"], wsad["d"])
        bohater3.tick(ikjl["5"], ikjl["2"], ikjl["1"], ikjl["3"])

        if bohater1.hitbox.colliderect(belki["wioska"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog7"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater1.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                miasto(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater1.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater1.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater1.hitbox.colliderect(belki["boss"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog6"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                boss(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater1.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog8"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater1.hitbox.colliderect(belki["zbrojownia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog5"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater1.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater1.hitbox.colliderect(belki["granica1"].hitbox):
            bohater1.x = bohater1.wczesniejszy_x
            bohater1.predkosc_lewo = 0
        else:
            bohater1.predkosc_lewo = 10

        if bohater1.hitbox.colliderect(belki["granica2"].hitbox):
            bohater1.y = bohater1.wczesniejszy_y
            bohater1.predkosc_gora = 0
        else:
            bohater1.predkosc_gora = 10

        if bohater1.hitbox.colliderect(belki["granica3"].hitbox):
            bohater1.x = bohater1.wczesniejszy_x
            bohater1.predkosc_dol = 0
        else:
            bohater1.predkosc_dol = 10

        if bohater1.hitbox.colliderect(belki["granica4"].hitbox):
            bohater1.y = bohater1.wczesniejszy_y
            bohater1.predkosc_prawo = 0
        else:
            bohater1.predkosc_prawo = 10

        bohater1.wczesniejszy_x = bohater1.x
        bohater1.wczesniejszy_y = bohater1.y

        if bohater2.hitbox.colliderect(belki["wioska"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog7"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater2.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                miasto(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater2.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater2.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater2.hitbox.colliderect(belki["boss"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog6"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                boss(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater2.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog8"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater2.hitbox.colliderect(belki["zbrojownia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog5"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater2.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater2.hitbox.colliderect(belki["granica1"].hitbox):
            bohater2.x = bohater2.wczesniejszy_x
            bohater2.predkosc_lewo = 0
        else:
            bohater2.predkosc_lewo = 10

        if bohater2.hitbox.colliderect(belki["granica2"].hitbox):
            bohater2.y = bohater2.wczesniejszy_y
            bohater2.predkosc_gora = 0
        else:
            bohater2.predkosc_gora = 10

        if bohater2.hitbox.colliderect(belki["granica3"].hitbox):
            bohater2.x = bohater2.wczesniejszy_x
            bohater2.predkosc_dol = 0
        else:
            bohater2.predkosc_dol = 10

        if bohater2.hitbox.colliderect(belki["granica4"].hitbox):
            bohater2.y = bohater2.wczesniejszy_y
            bohater2.predkosc_prawo = 0
        else:
            bohater2.predkosc_prawo = 10

        bohater2.wczesniejszy_x = bohater2.x
        bohater2.wczesniejszy_y = bohater2.y

        if bohater3.hitbox.colliderect(belki["wioska"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog7"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater3.hitbox.colliderect(belki["miasto"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog3"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                miasto(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater3.hitbox.colliderect(belki["las"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog1"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                las(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater3.hitbox.colliderect(belki["jaskinia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog2"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                jaskinia(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater3.hitbox.colliderect(belki["boss"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog6"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                boss(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater3.hitbox.colliderect(belki["drugi_swiat"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog8"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater3.hitbox.colliderect(belki["zbrojownia"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog5"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                pass

        if bohater3.hitbox.colliderect(belki["cmentarz"].hitbox):
            okno.blit(tlo2, (0, 500))
            okno.blit(teksty["dialog4"], (0, 500))
            przyciski["tak"].draw(okno)
            if przyciski["tak"].tick():
                cmentarz(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy)

        if bohater3.hitbox.colliderect(belki["granica1"].hitbox):
            bohater3.x = bohater3.wczesniejszy_x
            bohater3.predkosc_lewo = 0
        else:
            bohater3.predkosc_lewo = 10

        if bohater3.hitbox.colliderect(belki["granica2"].hitbox):
            bohater3.y = bohater3.wczesniejszy_y
            bohater3.predkosc_gora = 0
        else:
            bohater3.predkosc_gora = 10

        if bohater3.hitbox.colliderect(belki["granica3"].hitbox):
            bohater3.x = bohater3.wczesniejszy_x
            bohater3.predkosc_dol = 0
        else:
            bohater3.predkosc_dol = 10

        if bohater3.hitbox.colliderect(belki["granica4"].hitbox):
            bohater3.y = bohater3.wczesniejszy_y
            bohater3.predkosc_prawo = 0
        else:
            bohater3.predkosc_prawo = 10

        bohater3.wczesniejszy_x = bohater3.x
        bohater3.wczesniejszy_y = bohater3.y

        pygame.display.update()


def las(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy):
    run = True
    pauza = False
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "LAS", True, (255, 255, 255)),
              "Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255)),
              "Zdrowie_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie_przeciwnik['zdrowie1']}", True, (255, 255, 255)),
              "Oslona_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona_przeciwnik["oslona1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia_przeciwnik["demage1"]}', True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}
    
    bohater1 = Bohater(350, 550, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(350, 550, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(350, 550, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

    przeciwnik = Przeciwnik(650, 430, przeciwnicy["goblin"], zdrowie_przeciwnik["zdrowie1"], oslona_przeciwnik["oslona1"], obrazenia_przeciwnik["demage1"])

    tlo = pygame.image.load("Zdjęcia/tla/las.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (600, 0))

        okno.blit(teksty["Zdrowie"], (1188, 550))
        okno.blit(teksty["oslona"], (1200, 450))
        okno.blit(teksty["obrazenia"], (1173, 350))
        przeciwnik.draw(okno)
        okno.blit(teksty["Zdrowie_liczba_przeciwnik"], (1250, 600))
        okno.blit(teksty["Oslona_liczba_przeciwnik"], (1250, 500))
        okno.blit(teksty["Obrazenia_liczba_przeciwnik"], (1250, 400))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def cmentarz(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy):
    run = True
    pauza = False
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "CMENTARZ", True, (255, 255, 255)),
              "Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255)),
              "Zdrowie_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie_przeciwnik['zdrowie3']}", True, (255, 255, 255)),
              "Oslona_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona_przeciwnik["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia_przeciwnik["demage3"]}', True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(350, 550, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(350, 550, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(350, 550, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

    przeciwnik = Przeciwnik(700, 380, przeciwnicy["zniwiarz"], zdrowie_przeciwnik["zdrowie3"], oslona_przeciwnik["oslona3"], obrazenia_przeciwnik["demage3"])

    tlo = pygame.image.load("Zdjęcia/tla/cmentarz.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (450, 0))

        okno.blit(teksty["Zdrowie"], (1188, 550))
        okno.blit(teksty["oslona"], (1200, 450))
        okno.blit(teksty["obrazenia"], (1173, 350))
        przeciwnik.draw(okno)
        okno.blit(teksty["Zdrowie_liczba_przeciwnik"], (1250, 600))
        okno.blit(teksty["Oslona_liczba_przeciwnik"], (1250, 500))
        okno.blit(teksty["Obrazenia_liczba_przeciwnik"], (1250, 400))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def jaskinia(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy):
    run = True
    pauza = False
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "JASKINIA", True, (255, 255, 255)),
              "Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255)),
              "Zdrowie_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie_przeciwnik['zdrowie2']}", True, (255, 255, 255)),
              "Oslona_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona_przeciwnik["oslona2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia_przeciwnik["demage2"]}', True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(350, 550, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(350, 550, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(350, 550, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

    przeciwnik = Przeciwnik(600, 450, przeciwnicy["pajak"], zdrowie_przeciwnik["zdrowie2"], oslona_przeciwnik["oslona2"], obrazenia_przeciwnik["demage2"])

    tlo = pygame.image.load("Zdjęcia/tla/jaskinia.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (450, 0))

        okno.blit(teksty["Zdrowie"], (1188, 550))
        okno.blit(teksty["oslona"], (1200, 450))
        okno.blit(teksty["obrazenia"], (1173, 350))
        przeciwnik.draw(okno)
        okno.blit(teksty["Zdrowie_liczba_przeciwnik"], (1250, 600))
        okno.blit(teksty["Oslona_liczba_przeciwnik"], (1250, 500))
        okno.blit(teksty["Obrazenia_liczba_przeciwnik"], (1250, 400))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def miasto(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy):
    run = True
    pauza = False
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "MIASTO", True, (255, 255, 255)),
              "Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255)),
              "Zdrowie_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie_przeciwnik['zdrowie4']}", True, (255, 255, 255)),
              "Oslona_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona_przeciwnik["oslona4"]}', True, (255, 255, 255)),
              "Obrazenia_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia_przeciwnik["demage4"]}', True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(350, 550, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(350, 550, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(350, 550, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

    przeciwnik = Przeciwnik(650, 500, przeciwnicy["terrorysci"], zdrowie_przeciwnik["zdrowie4"], oslona_przeciwnik["oslona4"], obrazenia_przeciwnik["demage4"])

    tlo = pygame.image.load("Zdjęcia/tla/miasto.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (450, 0))

        okno.blit(teksty["Zdrowie"], (1188, 550))
        okno.blit(teksty["oslona"], (1200, 450))
        okno.blit(teksty["obrazenia"], (1173, 350))
        przeciwnik.draw(okno)
        okno.blit(teksty["Zdrowie_liczba_przeciwnik"], (1250, 600))
        okno.blit(teksty["Oslona_liczba_przeciwnik"], (1250, 500))
        okno.blit(teksty["Obrazenia_liczba_przeciwnik"], (1250, 400))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def boss(draw_bohater1, draw_bohater2, draw_bohater3, przeciwnicy):
    run = True
    pauza = False
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "BOSS", True, (255, 255, 255)),
              "Pauza": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "PAUZA", True, (255, 255, 255)),
              "Tekst2": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "Jeśli chcesz wrócic naciśnij klawisz `p`.", True, (255, 255, 255)),
              "Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255)),
              "Zdrowie_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie_przeciwnik['zdrowie5']}", True, (255, 255, 255)),
              "Oslona_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona_przeciwnik["oslona5"]}', True, (255, 255, 255)),
              "Obrazenia_liczba_przeciwnik": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia_przeciwnik["demage5"]}', True, (255, 255, 255)),
              }
    przyciski = {"wyjdz": Przyciski(500, 500, "Wyjdź"),
                 "graj": Przyciski(300, 500, "Przycisk")}

    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(350, 550, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(350, 550, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(350, 550, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

    przeciwnik = Przeciwnik(500, 300, przeciwnicy["boss"], zdrowie_przeciwnik["zdrowie5"], oslona_przeciwnik["oslona5"], obrazenia_przeciwnik["demage5"])

    tlo = pygame.image.load("Zdjęcia/tla/ostateczna_walka.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pauza = not pauza

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (450, 0))

        okno.blit(teksty["Zdrowie"], (1188, 550))
        okno.blit(teksty["oslona"], (1200, 450))
        okno.blit(teksty["obrazenia"], (1173, 350))
        przeciwnik.draw(okno)
        okno.blit(teksty["Zdrowie_liczba_przeciwnik"], (1230, 600))
        okno.blit(teksty["Oslona_liczba_przeciwnik"], (1250, 500))
        okno.blit(teksty["Obrazenia_liczba_przeciwnik"], (1250, 400))

        if draw_bohater1 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater1.draw(okno)
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))

        if pauza is True:
            okno.blit(teksty["Pauza"], (0, 0))
            okno.blit(teksty["Tekst2"], (0, 200))
            przyciski["wyjdz"].draw(okno)
            if przyciski["wyjdz"].tick():
                run = False
            pygame.display.update()
            continue

        pygame.display.update()


def zasady(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    tlo = pygame.image.load("Zdjęcia/tla/Lobby.png")
    teksty = {"Nazwa": pygame.font.Font.render(pygame.font.SysFont("arial", 50), "ZASADY", True, (255, 255, 255)),
              "Zasada1": pygame.font.Font.render(pygame.font.SysFont("arial", 30), "1. Rozgrywka się nie zapisuje.", True, (255, 255, 255)),
              "Zasada2": pygame.font.Font.render(pygame.font.SysFont("arial", 30), "2. Każdy level można zagrać tylko raz.", True, (255, 255, 255)),
             }
    przyciski = {"Graj": Przyciski(1000, 500, "Przycisk"),
                 "Wyjdz": Przyciski(1000, 600, "Wyjdź")
                 }
    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        okno.blit(tlo, (0, 0))
        okno.blit(teksty["Nazwa"], (0, 0))
        okno.blit(teksty["Zasada1"], (0, 100))
        okno.blit(teksty["Zasada2"], (0, 150))
        przyciski["Graj"].draw(okno)
        przyciski["Wyjdz"].draw(okno)

        if przyciski["Graj"].tick():
            lobby(draw_bohater1, draw_bohater2, draw_bohater3)
        if przyciski["Wyjdz"].tick():
            run = False

        pygame.display.update()


def lobby(draw_bohater1, draw_bohater2, draw_bohater3):
    run = True
    teksty = {"Zdrowie": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "ZDROWIE", True, (255, 255, 255)),
              "oslona": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OSLONA", True, (255, 255, 255)),
              "obrazenia": pygame.font.Font.render(pygame.font.SysFont("arial", 20), "OBRAZENIA", True, (255, 255, 255)),
              "Zdrowie_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f"{zdrowie['zdrowie1']}", True, (255, 255, 255)),
              "Zdrowie_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie2"]}', True, (255, 255, 255)),
              "Zdrowie_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{zdrowie["zdrowie3"]}', True, (255, 255, 255)),
              "Oslona_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona1"]}', True, (255, 255, 255)),
              "Oslona_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona2"]}', True, (255, 255, 255)),
              "Oslona_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{oslona["oslona3"]}', True, (255, 255, 255)),
              "Obrazenia_liczba1": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage1"]}', True, (255, 255, 255)),
              "Obrazenia_liczba2": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage2"]}', True, (255, 255, 255)),
              "Obrazenia_liczba3": pygame.font.Font.render(pygame.font.SysFont("arial", 20), f'{obrazenia["demage3"]}', True, (255, 255, 255))
              }
    sterowanie = {"WSAD": pygame.image.load("Zdjęcia/sterowanie1.png"),
                  "GLDP": pygame.image.load("Zdjęcia/sterowanie2.png"),
                  "IKJL": pygame.image.load("Zdjęcia/sterowanie3.png")
                  }
    postacie = {"postac1": "Bohater1",
                "postac2": "Bohater2",
                "postac3": "Bohater3"}

    bohater1 = Bohater(500, 500, postacie["postac1"], zdrowie["zdrowie1"], obrazenia["demage1"], oslona["oslona1"])
    bohater2 = Bohater(500, 500, postacie["postac2"], zdrowie["zdrowie2"], obrazenia["demage2"], oslona["oslona2"])
    bohater3 = Bohater(500, 500, postacie["postac3"], zdrowie["zdrowie3"], obrazenia["demage3"], oslona["oslona3"])

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
            okno.blit(teksty["Zdrowie_liczba1"], (5, 600))
            okno.blit(teksty["Oslona_liczba1"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba1"], (5, 400))
            okno.blit(sterowanie["WSAD"], (1000, 0))

        if draw_bohater2 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater2.draw(okno)
            okno.blit(teksty["Zdrowie_liczba2"], (5, 600))
            okno.blit(teksty["Oslona_liczba2"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba2"], (5, 400))
            okno.blit(sterowanie["GLDP"], (1000, 0))

        if draw_bohater3 is True:
            okno.blit(teksty["Zdrowie"], (0, 550))
            okno.blit(teksty["oslona"], (0, 450))
            okno.blit(teksty["obrazenia"], (0, 350))
            bohater3.draw(okno)
            okno.blit(teksty["Zdrowie_liczba3"], (5, 600))
            okno.blit(teksty["Oslona_liczba3"], (5, 500))
            okno.blit(teksty["Obrazenia_liczba3"], (5, 400))
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
            zasady(draw_bohater1=False, draw_bohater2=False, draw_bohater3=False)

        if przyciski["Wyjdz"].tick():
            run = False

        okno.blit(pygame.image.load("Zdjęcia/tla/tło początkowe.png"), (0, 0))
        przyciski["Graj"].draw(okno)
        przyciski["Wyjdz"].draw(okno)
        pygame.display.update()


if __name__ == '__main__':
    main()
