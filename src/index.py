from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
from .algo import algorajapinta
# import logic.traversallogic as logic
from .logic import mapreader as reader
import argparse
from random import randint
import time

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    parser = argparse.ArgumentParser(description="Käynnistysasetukset")
    parser.add_argument('--testaa_ajat', action='store_true', help='Ajastustestit pääprojektin sijaan')

    args = parser.parse_args()

    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    runtime_astar = astar.AStar(kartta,(0,0),(0,0))
    runtime_jps = jps.JPS(kartta,(0,0),(0,0))
    algo = algorajapinta.AlgoRajapinta([runtime_astar,runtime_jps])

    if args.testaa_ajat:
        aikavertailu(kartta, algo)
    else:
        ui.run_ui(algo, True)

def aikavertailu(kartta, algo):
    pisteet = kartta.kaikki_kuljettavat_pisteet()
    virhe = False
    nopeampi_astar = 0
    testit = 20
    for i in range(testit):
        alku = pisteet[randint(0, len(pisteet))]
        loppu = pisteet[randint(0, len(pisteet))]
        print(f"{i+1}. Testataan reitinhaku pisteestä {alku} pisteeseen {loppu}")
        print("A*:")
        algo.vaihda_alku(alku)
        algo.vaihda_loppu(loppu)
        aloitusaika = time.time()
        algo.aloita_algo()
        lopetusaika = time.time()
        kokonaisaika_astar = lopetusaika-aloitusaika
        pituus_astar = round(algo.palauta_pituus(),3)
        print(f"Löydettiin {pituus_astar} mittainen reitti {kokonaisaika_astar} sekunnissa")
        algo.vaihda_algo()
        print("JPS:")
        algo.vaihda_alku(alku)
        algo.vaihda_loppu(loppu)
        aloitusaika = time.time()
        algo.aloita_algo()
        lopetusaika = time.time()
        kokonaisaika_jps = lopetusaika-aloitusaika
        pituus_jps = round(algo.palauta_pituus(),3)
        print(f"Löydettiin {pituus_jps} mittainen reitti {kokonaisaika_jps} sekunnissa")
        if kokonaisaika_astar < kokonaisaika_jps:
            nopeampi_astar += 1
        if pituus_astar == pituus_jps:
            print("Pituudet täsmäävät\n")
        else:
            print("PITUUKSIEN TÄSMÄÄVYYSVIRHE!!\n")
            virhe = True
            virheet = []
            virheet.append(i+1)
        algo.vaihda_algo()
    if virhe:
        print("KAIKKI LÖYDETYT PITUUDET EIVÄT OLLEET SAMAN MITTAISIA")
        print(virheet)
        print("")
    else:
        print("Ei pituusvirheitä\n")
    if nopeampi_astar == 0:
        jps_voittoprosentti = 100
    else:
        jps_voittoprosentti = round(((testit-nopeampi_astar)/testit)*100)
    print(f"JPS oli nopeampi kuin A* {jps_voittoprosentti}% testeistä eli {testit-nopeampi_astar} testissä")



if __name__ == "__main__":   
    main()

