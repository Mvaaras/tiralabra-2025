from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
# import logic.traversallogic as logic
from .logic import mapreader as reader

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    testi_astar = astar.AStar((7,105),(235,177),kartta)
    for point in testi_astar.astar():
        x =point[0]
        y = point[1]
        kartta.vaihda_piste(x,y)
    
    ui.run_ui(kartta)
    return

if __name__ == "__main__":
    main()