from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
# import logic.traversallogic as logic
from .logic import mapreader as reader

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    helppokartta = reader.luo_polusta("src/tests/testassets/testmap.map",20)
    testi_astar = astar.AStar(kartta,(7,105),(235,177))
    testi_jps = jps.JPS(kartta,(0,0),(0,0))

    ui.run_ui(testi_jps)

if __name__ == "__main__":
    main()
