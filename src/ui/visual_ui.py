import pygame
from src.logic.mapreader import AsciiKartta as kartta
from src.logic.mapreader import luo_polusta

# Reitinhaun visualisointi

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