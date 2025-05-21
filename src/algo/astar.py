#A* Algoritmin toteutus
from math import sqrt
from queue import PriorityQueue

class AStar:
    def __init__(self, kartta,alku=(0,0),loppu=(0,0)):
        self.alku = alku
        self.loppu = loppu
        self.kartta = kartta
        self.edellinen = {}
        self.lyhin_reitti_pisteeseen = {}
        self.jonossa = {}
    
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

        #tarkistetaan ettei aloiteta tai lopeteta seinän sisään.
        if (self.kartta.piste(self.alku) != "." 
            or self.kartta.piste(self.loppu) != "."):
            return []

        return self.astar()

    def astar(self):

        while not self.jono.empty():
            #self.jonossa on aina oletettu maksimimatka loppupisteeseen jonka mukaan
            #valitaan lupaavin piste tutkia, sekä piste itse.

            #muuttujaan "tutkittava" tallennetaan ainoastaan piste.
            tutkittava = self.jono.get()[1]
            self.jonossa[tutkittava] = False
            x = tutkittava[0]
            y = tutkittava[1]

            #jos on saavutettu loppupiste, palautetaan löydetty reitti
            if tutkittava == self.loppu:
                return self.palauta_reitti()

            #haetaan tutkittavan pisteen naapurit ja läpikäydään ne. hae_suunnat palauttaa listan jossa 
            #on tuplena pisteen koordinaatit (tuple) ja matka pisteeseen siirtymiseen (kulmittainen tai suora)
            naapurit = self.kartta.hae_suunnat(x,y)
            for naapuri in naapurit:
                naapuri_piste = naapuri[0]
                naapuri_etaisyys = naapuri[1]
                oletettu_etaisyys = self.lyhin_reitti_pisteeseen[tutkittava] + naapuri_etaisyys
                try:
                    etaisyys = self.lyhin_reitti_pisteeseen[naapuri_piste]
                    if etaisyys > oletettu_etaisyys :
                        self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
                except:
                    self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
        return []

    #apumetodeja joita varsinainen algo kutsuu

    def paivita_etaisyys(self, piste, naapuri, etaisyys):
        self.edellinen[piste] = naapuri
        self.lyhin_reitti_pisteeseen[piste] = etaisyys
        try:
            if not self.jonossa[piste]:
                self.lisaa_jonoon(piste,etaisyys)
        except:
            self.lisaa_jonoon(piste,etaisyys)
    
    def lisaa_jonoon(self, piste,etaisyys):
        self.jono.put((etaisyys+self.minimietaisyys(piste),piste))
        self.jonossa[piste] = True


    def minimietaisyys(self, a):
        x_etaisyys = abs(a[0]-self.loppu[0])
        y_etaisyys = abs(a[1]-self.loppu[1])
        kokonaismatka = x_etaisyys + y_etaisyys
        suoraan = abs(x_etaisyys-y_etaisyys)
        vinosuuntaan = kokonaismatka-suoraan
        return suoraan + (vinosuuntaan*(sqrt(2)))

    def palauta_reitti(self):
        reitti = []
        piste = self.loppu
        while piste != "alku":
            reitti.append(piste)
            piste = self.edellinen[piste]
        reitti.reverse()
        return reitti



