#A* Algoritmin toteutus
from math import sqrt
from queue import PriorityQueue

TOSI_ISO_LUKU = 100000000

class AStar:
    def __init__(self, kartta,alku=(0,0),loppu=(0,0)):
        self.alku = alku
        self.loppu = loppu
        self.kartta = kartta
        self.edellinen = {}
        self.lyhin_reitti_pisteeseen = {}
        self.jonossa = {}
        self.jono = PriorityQueue()

        self.reittidata = {}
        self.kaikki_vieraillut_pisteet = set()

    def vaihda_alku(self,x,y=None):
        self.alku = self._tarkista_piste(x,y)

    def vaihda_loppu(self, x,y=None):
        self.loppu = self._tarkista_piste(x,y)

    def _tarkista_piste(self,x,y=None):
        if y is None:
            return x
        return (x,y)

    #Varsinainen algoritmin suoritus tapahtuu täällä

    def aloita_astar(self):
        self.edellinen = {self.alku:"alku"}
        self.lyhin_reitti_pisteeseen = {self.alku:0}
        self.jono = PriorityQueue()
        self.jono.put((self.minimietaisyys(self.alku),self.alku))
        self.jonossa = {self.alku:True}

        self.kaikki_vieraillut_pisteet = set()
        self.kaikki_vieraillut_pisteet.add(self.alku)
        self.reittidata = {"reitti":[],
                           "vieraillut":self.kaikki_vieraillut_pisteet,
                           "pituus":TOSI_ISO_LUKU}

        #tarkistetaan ettei aloiteta tai lopeteta seinän sisään.
        if (self.kartta.piste(self.alku) != "."
            or self.kartta.piste(self.loppu) != "."):
            return self.reittidata

        return self.astar()

    def astar(self):
        while not self.jono.empty():
            #self.jonossa on aina oletettu maksimimatka loppupisteeseen jonka mukaan
            #valitaan lupaavin piste tutkia, sekä piste itse.

            #muuttujaan "tutkittava" tallennetaan ainoastaan piste.
            tutkittava = self.jono.get()[1]
            self.kaikki_vieraillut_pisteet.add(tutkittava)
            self.jonossa[tutkittava] = False
            x = tutkittava[0]
            y = tutkittava[1]

            #jos on saavutettu loppupiste, palautetaan löydetty reitti
            if tutkittava == self.loppu:
                return self.palauta_reitti()

            #haetaan tutkittavan pisteen naapurit ja läpikäydään ne. hae_suunnat palauttaa
            #listan jossa on tuplena pisteen koordinaatit (tuple)
            #ja matka pisteeseen siirtymiseen (kulmittainen tai suora)
            naapurit = self.kartta.hae_suunnat(x,y)
            for naapuri in naapurit:
                naapuri_piste = naapuri[0]
                naapuri_etaisyys = naapuri[1]
                oletettu_etaisyys = self.lyhin_reitti_pisteeseen[tutkittava] + naapuri_etaisyys
                try:
                    etaisyys = self.lyhin_reitti_pisteeseen[naapuri_piste]
                    if etaisyys > oletettu_etaisyys :
                        self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
                except KeyError:
                    self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
        return self.reittidata

    #apumetodeja joita varsinainen algo kutsuu

    def paivita_etaisyys(self, piste, naapuri, etaisyys):
        self.edellinen[piste] = naapuri
        self.lyhin_reitti_pisteeseen[piste] = etaisyys
        self.lisaa_jonoon(piste,etaisyys)

    def lisaa_jonoon(self, piste,etaisyys):
        self.jono.put((etaisyys+self.minimietaisyys(piste),piste))
        self.jonossa[piste] = True

    def minimietaisyys(self, a):
        #heuristiikkafunktio
        x_etaisyys = abs(a[0]-self.loppu[0])
        y_etaisyys = abs(a[1]-self.loppu[1])
        diagonaalinen_etaisyys = min(x_etaisyys,y_etaisyys)
        suora_etaisyys = max(x_etaisyys,y_etaisyys) - diagonaalinen_etaisyys
        return diagonaalinen_etaisyys*sqrt(2)+suora_etaisyys

    def palauta_reitti(self):
        reitti = []
        reitin_pituus = 0
        piste = self.loppu
        while piste != "alku":
            reitti.append(piste)
            reitin_pituus += self.onko_kulmittainen(piste,self.edellinen[piste])
            piste = self.edellinen[piste]
        reitti.reverse()
        self.reittidata["reitti"] = reitti
        self.reittidata["pituus"] = reitin_pituus
        return self.reittidata

    def onko_kulmittainen(self,piste,edellinen):
        if edellinen == "alku": 
            return 0
        suunta = (piste[0]-edellinen[0],piste[1]-edellinen[1])
        if 0 in suunta:
            return 1
        return sqrt(2)


    def aloita(self):
        return self.aloita_astar()

    def palauta_nimi(self):
        return "A*"
