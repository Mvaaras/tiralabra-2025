import argparse
from random import randint
import time
from .ui import visual_ui as ui
from .algo import astar
from .algo import jps
from .algo import algorajapinta
from .logic import mapreader as reader

#Käynnistys, kutsuu pääasiassa muita metodeja

def main():
    parser = argparse.ArgumentParser(description="Käynnistysasetukset")
    parser.add_argument('--testaa_ajat', action='store_true',
                        help='Ajastustestit pääprojektin sijaan')

    args = parser.parse_args()

    kartta = reader.luo_polusta("src/assets/arena2.map",4)
    runtime_astar = astar.AStar(kartta,(0,0),(0,0))
    runtime_jps = jps.JPS(kartta,(0,0),(0,0))
    algo = algorajapinta.AlgoRajapinta([runtime_astar,runtime_jps])

    if args.testaa_ajat:
        pisteet = kartta.kaikki_kuljettavat_pisteet()
        aikavertailu(algo,pisteet)
    else:
        ui.run_ui(algo)

def aikavertailu(algo,pisteet):
    nopeampi_astar = 0
    virheet = []
    testit = 50
    for i in range(testit):
        alku = pisteet[randint(0, len(pisteet))]
        loppu = pisteet[randint(0, len(pisteet))]
        print(f"{i+1}. Testataan reitinhaku pisteestä {alku} pisteeseen {loppu}")
        kokonaisaika_astar, pituus_astar  = vertaa_aika(algo,alku,loppu)
        algo.vaihda_algo()
        kokonaisaika_jps, pituus_jps = vertaa_aika(algo,alku,loppu)
        if kokonaisaika_astar < kokonaisaika_jps:
            nopeampi_astar += 1
        if pituus_astar == pituus_jps:
            print("Pituudet täsmäävät\n")
        else:
            print("PITUUKSIEN TÄSMÄÄVYYSVIRHE!!\n")
            virheet.append(i+1)
        algo.vaihda_algo()
    aikavertailu_loppuraportti(virheet, nopeampi_astar,testit)

def vertaa_aika(algo,alku,loppu):
    print(f"{algo.nimi()}:")
    algo.vaihda_alku(alku)
    algo.vaihda_loppu(loppu)
    aloitusaika = time.time()
    algo.aloita_algo()
    lopetusaika = time.time()
    kokonaisaika = lopetusaika-aloitusaika
    pituus = round(algo.palauta_pituus(),3)
    print(f"Löydettiin {pituus} mittainen reitti {kokonaisaika} sekunnissa")
    return kokonaisaika,pituus

def aikavertailu_loppuraportti(virheet, nopeampi_astar,testit):
    if len(virheet) != 0:
        print("KAIKKI LÖYDETYT PITUUDET EIVÄT OLLEET SAMAN MITTAISIA")
        print(virheet)
        print("")
    else:
        print("Ei pituusvirheitä\n")
    if nopeampi_astar == 0:
        jps_voittoprosentti = 100
    else:
        jps_voittoprosentti = round(((testit-nopeampi_astar)/testit)*100)
    print(f"JPS oli nopeampi kuin A* {jps_voittoprosentti}% testeistä", end =" ")
    print(f"({testit-nopeampi_astar} testissä)")



if __name__ == "__main__":
    main()
