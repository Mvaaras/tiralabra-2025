from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
from .algo import algorajapinta
# import logic.traversallogic as logic
from .logic import mapreader as reader

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    helppokartta = reader.luo_polusta("src/tests/testassets/testmap.map",20)
    testi_astar = astar.AStar(kartta,(0,0),(0,0))
    testi_jps = jps.JPS(kartta,(0,0),(0,0))
    algo = algorajapinta.AlgoRajapinta([testi_astar,testi_jps])

    ui.run_ui(algo, True)

if __name__ == "__main__":
    main()
