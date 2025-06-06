import pygame
from src.logic.mapreader import luo_polusta

# Reitinhaun visualisointi
def ui_testaus():
    ui_kartta = luo_polusta("src/assets/arena2.map",4)
    pixel_size = ui_kartta.pikselikoko

    pygame.init()

    screen = pygame.display.set_mode((ui_kartta.leveys*pixel_size,ui_kartta.korkeus*pixel_size))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit


        screen.fill("white")

        #Kartan piirtäminen
        for y in range(ui_kartta.korkeus):
            for x in range(ui_kartta.leveys):
                pikseli = pygame.Rect(x*pixel_size,y*pixel_size,pixel_size,pixel_size)
                pygame.draw.rect(screen, ui_kartta.hae_vari(x,y), pikseli)

        pygame.display.flip() 
        clock.tick(60)  

def run_ui(algo,debug=False):
    kartta = algo.kartta()
    pixel_size = kartta.pikselikoko
    pygame.init()

    screen = pygame.display.set_mode((kartta.leveys*pixel_size,kartta.korkeus*pixel_size))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y =  pygame.mouse.get_pos()
                oikea_x = x // pixel_size
                oikea_y = y // pixel_size
                if debug: print(str(oikea_x),str(oikea_y))
                napit = pygame.mouse.get_pressed()
                if napit[0]:
                    algo.vaihda_alku(oikea_x,oikea_y)
                    kartta.flush()
                if napit[2]:
                    algo.vaihda_loppu(oikea_x,oikea_y)
                    kartta.flush()
                reitti = algo.aloita_algo()
                piirra_reitti(kartta, algo.palauta_vieraillut(),"V")
                piirra_reitti(kartta,reitti)
                piirra_reitti(kartta, algo.palauta_extra(),"E")


        screen.fill("white")

        #Kartan piirtäminen
        for y in range(kartta.korkeus):
            for x in range(kartta.leveys):
                pikseli = pygame.Rect(x*pixel_size,y*pixel_size,pixel_size,pixel_size)
                pygame.draw.rect(screen, kartta.hae_vari(x,y), pikseli)

        pygame.display.flip() 
        clock.tick(60)

def piirra_reitti(kartta,reitti,vaihdettava="*"):
    for point in reitti:
        x = point[0]
        y = point[1]
        kartta.vaihda_piste(x,y,vaihdettava)
