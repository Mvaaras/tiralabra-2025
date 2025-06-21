import pygame
from src.logic.mapreader import luo_polusta

YLAMENU_KORKEUS = 40

# Reitinhaun visualisointi

def run_ui(algo,debug=False):
    kartta = algo.kartta()
    pixel_size = kartta.pikselikoko
    pygame.init()


    fontti = pygame.font.SysFont(None, 30)
    vaihda_karttaa_teksti = fontti.render("Klikkaa tästä vaihtaaksesi algoritmia", True, "Black","azure4")

    screen = pygame.display.set_mode((kartta.leveys*pixel_size,kartta.korkeus*pixel_size+YLAMENU_KORKEUS))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y =  pygame.mouse.get_pos()
                if y > YLAMENU_KORKEUS:
                    oikea_x = x // pixel_size
                    oikea_y = (y-YLAMENU_KORKEUS) // pixel_size
                    if debug: print(str(oikea_x),str(oikea_y))
                    napit = pygame.mouse.get_pressed()
                    if napit[0]:
                        algo.vaihda_alku(oikea_x,oikea_y)
                        kartta.flush()
                    if napit[2]:
                        algo.vaihda_loppu(oikea_x,oikea_y)
                        kartta.flush()
                else:
                    algo.vaihda_algo()
                reitti = algo.aloita_algo()
                piirra_reitti(kartta, algo.palauta_vieraillut(),"V")
                piirra_reitti(kartta,reitti)
                piirra_reitti(kartta, algo.palauta_extra(),"E")


        screen.fill("white")

        #Kartan piirtäminen
        for y in range(kartta.korkeus):
            for x in range(kartta.leveys):
                pikseli = pygame.Rect(x*pixel_size,y*pixel_size+YLAMENU_KORKEUS,pixel_size,pixel_size)
                pygame.draw.rect(screen, kartta.hae_vari(x,y), pikseli)
        
        #Menun piirtäminen
        screen.blit(vaihda_karttaa_teksti, (10,10))
        screen.blit(fontti.render(algo.nimi(), True, "Black","azure4"), (kartta.leveys*pixel_size-50,10))
        

        pygame.display.flip() 
        clock.tick(15)

def piirra_reitti(kartta,reitti,vaihdettava="*"):
    for point in reitti:
        x = point[0]
        y = point[1]
        kartta.vaihda_piste(x,y,vaihdettava)