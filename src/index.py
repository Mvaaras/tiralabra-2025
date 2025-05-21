from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
# import logic.traversallogic as logic
from .logic import mapreader as reader

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    testi_astar = astar.AStar(kartta,(7,105),(235,177))
    """for point in testi_astar.aloita_astar():
        x =point[0]
        y = point[1]
        kartta.vaihda_piste(x,y)"""
    
    ui.run_ui(testi_astar)
    return

if __name__ == "__main__":
    main()