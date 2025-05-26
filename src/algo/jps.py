#Jump Point Search Algoritmin toteutus

from math import sqrt
from queue import PriorityQueue

class JPS:
    def __init__(self, kartta,alku=(0,0),loppu=(0,0)):
        self.alku = alku
        self.loppu = loppu
        self.kartta = kartta
        self.edellinen = {}
        self.lyhin_reitti_pisteeseen = {}
        self.jonossa = {}
        self.jono = PriorityQueue()

    def vaihda_alku(self,x,y=None):
        self.alku = self._tarkista_piste(x,y)

    def vaihda_loppu(self, x,y=None):
        self.loppu = self._tarkista_piste(x,y)

    def _tarkista_piste(self,x,y=None):
        if y is None:
            return x
        return (x,y)

    #Varsinainen algoritmin suoritus tapahtuu täällä

    def aloita_jps(self):

        self.edellinen = {self.alku:"alku"}
        self.lyhin_reitti_pisteeseen = {self.alku:0}
        self.jono = PriorityQueue()
        self.jono.put((self.minimietaisyys(self.alku),self.alku))
        self.jonossa = {self.alku:True}

        #tarkistetaan ettei aloiteta tai lopeteta seinän sisään.
        if (self.kartta.piste(self.alku) != "."
            or self.kartta.piste(self.loppu) != "."):
            return []

        return self.jps()

    def jps(self):

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

            #haetaan suunta josta tutkittava piste on peräisin. Jos suuntaa ei ole, kartta olettaa suunnan olevan "kaikki"
            hyppysuunnat = self.karsi_suunnat(self.hae_tulosuunta(self.edellinen[tutkittava], tutkittava),x,y)
            for suunta in hyppysuunnat:
                loydetyt_hypyt = self.hyppaa_eteenpain(suunta, tutkittava)
            """for naapuri in naapurit:
                naapuri_piste = naapuri[0]
                naapuri_etaisyys = naapuri[1]
                oletettu_etaisyys = self.lyhin_reitti_pisteeseen[tutkittava] + naapuri_etaisyys
                try:
                    etaisyys = self.lyhin_reitti_pisteeseen[naapuri_piste]
                    if etaisyys > oletettu_etaisyys :
                        self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
                except KeyError:
                    self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)"""
        return []


    #apumetodeja joita varsinainen algo kutsuu.

    #nimenomaan jps varten luodut metodit ensin, nämä tässä ovat vielä työn alla

    def hyppaa_eteenpain(self, suunta, tutkittava):
        if 0 in suunta:
            return self.hyppaa_eteenpain_vinoon(suunta, tutkittava)
        return self.hyppaa_eteenpain_suoraan(suunta, tutkittava)
    
    def hyppaa_eteenpain_vinoon(self, suunta, tutkittava):
        loydetyt_pisteet = []
        loppu = False
        nykyinen_hyppypiste = tutkittava
        while True:
            seuraava_piste = self.kartta.hae_suunnat(tutkittava[0],tutkittava[1],((suunta, True)))
            if not seuraava_piste:
                break
    #JATKA TÄSTÄ!!!!


    def hae_tulosuunta(self, edellinen, piste):
        if edellinen == "alku":
            return "alku"
        edellinen_x = edellinen[0]
        edellinen_y = edellinen[1]
        x = piste[0]
        y = piste[1]
        return (x-edellinen_x,y-edellinen_y)

    def karsi_suunnat(self, suunta,x,y):
        suunnat = []
        if suunta == "alku":
            # pisteet on lista pisteitä ja etäisyyksiä yksittäisestä pisteestä siihen
            pisteet = self.kartta.hae_suunnat(x,y,((1,-1,True),(1,1,True),(-1,1,True),(-1,-1,True)))
            for piste in pisteet:
                suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
            return suunnat
        if not suunnat[0] == 0 and not suunnat[1] == 0:
            pisteet = self.kartta.hae_suunnat(x,y,((suunta[0],0,False),(0,suunta[1],False),(suunta, True)))
            for piste in pisteet:
                suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
        else:
            piste = self.kartta.hae_suunnat(x,y,((suunta,False)))[0]
            suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
        return suunnat
    
    #muut apumetodit

    def paivita_etaisyys(self, piste, naapuri, etaisyys):
        self.edellinen[piste] = naapuri
        self.lyhin_reitti_pisteeseen[piste] = etaisyys
        try:
            if not self.jonossa[piste]:
                self.lisaa_jonoon(piste,etaisyys)
        except KeyError:
            self.lisaa_jonoon(piste,etaisyys)

    def lisaa_jonoon(self, piste,etaisyys):
        self.jono.put((etaisyys+self.minimietaisyys(piste),piste))
        self.jonossa[piste] = True

    def minimietaisyys(self, a):
        x_etaisyys = abs(a[0]-self.loppu[0])
        y_etaisyys = abs(a[1]-self.loppu[1])
        return sqrt(x_etaisyys**2+y_etaisyys**2)

    def palauta_reitti(self):
        reitti = []
        piste = self.loppu
        while piste != "alku":
            reitti.append(piste)
            piste = self.edellinen[piste]
        reitti.reverse()
        return reitti
