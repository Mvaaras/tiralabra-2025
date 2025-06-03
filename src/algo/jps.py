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
                for hyppy in loydetyt_hypyt:
                    naapuri_piste = hyppy
                    naapuri_etaisyys = self.hae_etaisyys(tutkittava, hyppy, suunta)
                    oletettu_etaisyys = self.lyhin_reitti_pisteeseen[tutkittava] + naapuri_etaisyys
                    try:
                        etaisyys = self.lyhin_reitti_pisteeseen[naapuri_piste]
                        if etaisyys > oletettu_etaisyys :
                            self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
                    except KeyError:
                        self.paivita_etaisyys(naapuri_piste,tutkittava,oletettu_etaisyys)
        return []


    #apumetodeja joita varsinainen algo kutsuu.

    #nimenomaan jps varten luodut metodit ensin, nämä tässä ovat vielä työn alla

    def hyppaa_eteenpain(self, suunta, tutkittava):
        if 0 in suunta:
            return self.hyppaa_eteenpain_suoraan(suunta, tutkittava)
        return self.hyppaa_eteenpain_vinoon(suunta, tutkittava)
    
    def hyppaa_eteenpain_vinoon(self, suunta, tutkittava):
        nykyinen_hyppypiste = tutkittava
        loydetyt_suunnat = []
        suorat_suunnat = [(suunta[0],0),(0,suunta[1])]
        for suora_suunta in suorat_suunnat:
            loydetyt_suorat_hypyt = self.hyppaa_eteenpain_suoraan(suora_suunta, nykyinen_hyppypiste)
            loydetyt_suunnat.extend(loydetyt_suorat_hypyt)
        while True:
            seuraava_piste = self.kartta.hae_suunnat(nykyinen_hyppypiste[0],nykyinen_hyppypiste[1],[suunta])
            if not seuraava_piste:
                break
            nykyinen_hyppypiste = seuraava_piste[0][0]
            if nykyinen_hyppypiste == self.loppu:
                loydetyt_suunnat.append(nykyinen_hyppypiste)
                break
            for suora_suunta in suorat_suunnat:
                if self.hyppaa_eteenpain_suoraan(suora_suunta, nykyinen_hyppypiste):
                    loydetyt_suunnat.append(nykyinen_hyppypiste)
                    break
            if self.vino_pakotettu_naapuri(nykyinen_hyppypiste,suunta):
                loydetyt_suunnat.append(nykyinen_hyppypiste)
                break
        return loydetyt_suunnat
    
    def hyppaa_eteenpain_suoraan(self, suunta, tutkittava):
        nykyinen_hyppypiste = tutkittava
        while True:
            seuraava_piste = self.kartta.hae_suunnat(nykyinen_hyppypiste[0],nykyinen_hyppypiste[1],[suunta])
            if not seuraava_piste:
                break
            nykyinen_hyppypiste = seuraava_piste[0][0]
            if nykyinen_hyppypiste == self.loppu:
                return[nykyinen_hyppypiste]
            if self.suora_pakotettu_naapuri(nykyinen_hyppypiste, suunta):
                return [nykyinen_hyppypiste]
        return []
    
    def vino_pakotettu_naapuri(self, tutkittava, suunta):
        tarkistettavat_suunnat = []
        for este in self.hae_pakotetut_vinot_esteet(suunta):
            tarkistettavat_suunnat.append(este)
        for naapuri in self.hae_pakotetut_vinot_naapurit(suunta):
            tarkistettavat_suunnat.append(naapuri)
        tarkistettavat_pisteet = []
        for piste in self.kartta.hae_suunnat(tutkittava[0],tutkittava[1],tarkistettavat_suunnat):
            tarkistettavat_pisteet.append(piste[0])
        if not (tutkittava[0]+tarkistettavat_suunnat[0][0],tutkittava[1]+tarkistettavat_suunnat[0][1]) in tarkistettavat_pisteet:
            if (tutkittava[0]+tarkistettavat_suunnat[3][0],tutkittava[1]+tarkistettavat_suunnat[3][1]) in tarkistettavat_pisteet:
                return True
        if not (tutkittava[0]+tarkistettavat_suunnat[1][0],tutkittava[1]+tarkistettavat_suunnat[1][1]) in tarkistettavat_pisteet:
            if (tutkittava[0]+tarkistettavat_suunnat[2][0],tutkittava[1]+tarkistettavat_suunnat[2][1]) in tarkistettavat_pisteet:
                return True
        return False
    
    def hae_pakotetut_vinot_esteet(self, suunta):
        return [(0-suunta[0],suunta[1]-suunta[1]),(suunta[0]-suunta[0],0-suunta[1])]

    def hae_pakotetut_vinot_naapurit(self,suunta):
        return [(suunta[0]*2-suunta[0],0-suunta[1]),(0-suunta[0],suunta[1]*2-suunta[1])]
    
    def suora_pakotettu_naapuri(self, tutkittava, suunta):
        tarkistettavat_suunnat = []
        for este in self.hae_pakotetut_suorat_esteet(suunta):
            tarkistettavat_suunnat.append(este)
        for naapuri in self.hae_pakotetut_suorat_naapurit(suunta):
            tarkistettavat_suunnat.append(naapuri)
        tarkistettavat_pisteet = []
        for piste in self.kartta.hae_suunnat(tutkittava[0],tutkittava[1],tarkistettavat_suunnat):
            tarkistettavat_pisteet.append(piste[0])
        if not (tutkittava[0]+tarkistettavat_suunnat[0][0],tutkittava[1]+tarkistettavat_suunnat[0][1]) in tarkistettavat_pisteet:
            if (tutkittava[0]+tarkistettavat_suunnat[2][0],tutkittava[1]+tarkistettavat_suunnat[2][1]) in tarkistettavat_pisteet:
                return True
        if not (tutkittava[0]+tarkistettavat_suunnat[1][0],tutkittava[1]+tarkistettavat_suunnat[1][1]) in tarkistettavat_pisteet:
            if (tutkittava[0]+tarkistettavat_suunnat[3][0],tutkittava[1]+tarkistettavat_suunnat[3][1]) in tarkistettavat_pisteet:
                return True
        return False

    def hae_pakotetut_suorat_esteet(self, suunta):
        return [(suunta[1],suunta[0]),(suunta[1]*(-1),suunta[0]*(-1))]

    def hae_pakotetut_suorat_naapurit(self, suunta):
        # palauttaa oikeat pakotetut naapurit suhteessa suoraan liikkumasuuntaan tuplena "suunta"
        # kaavasta jossa tätä käytetään on lyhyt memo dokumentaatiossa ja sen oikeellisuus on varmistettu testeillä
        pakotetut_suorat_naapurit = [(suunta[0]+(suunta[0]+suunta[1])*(1-abs(suunta[0])),
                                      suunta[1]+(suunta[0]+suunta[1])*abs(suunta[0])),
                    (suunta[0]-(suunta[0]+suunta[1])*(1-abs(suunta[0])),
                     suunta[1]-(suunta[0]+suunta[1])*abs(suunta[0]))]
        return pakotetut_suorat_naapurit



    def hae_tulosuunta(self, edellinen, piste):
        if edellinen == "alku":
            return "alku"
        edellinen_x = edellinen[0]
        edellinen_y = edellinen[1]
        x = piste[0]
        y = piste[1]
        return self.normalisoi_suunta((x-edellinen_x,y-edellinen_y))
    
    def normalisoi_suunta(self, suunta):
        return ((suunta[0] > 0) - (suunta[0] < 0),(suunta[1] > 0) - (suunta[1] < 0))


    def karsi_suunnat(self, edellinen_suunta,x,y):
        suunnat = []
        if edellinen_suunta == "alku":
            # pisteet on lista pisteitä ja etäisyyksiä yksittäisestä pisteestä siihen
            pisteet = self.kartta.hae_suunnat(x,y)
            for piste in pisteet:
                suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
            return suunnat
        if not 0 in edellinen_suunta:
            pisteet = self.kartta.hae_suunnat(x,y,((edellinen_suunta[0],0),(0,edellinen_suunta[1]),edellinen_suunta))
            for piste in pisteet:
                suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
            if self.vino_pakotettu_naapuri((x,y),edellinen_suunta):
                naapuri_pisteet = self.kartta.hae_suunnat(x,y,self.hae_pakotetut_vinot_naapurit(edellinen_suunta))
                for naapuri_piste in naapuri_pisteet:
                    suunnat.append(self.hae_tulosuunta((x,y),naapuri_piste[0]))
        else:
            piste = self.kartta.hae_suunnat(x,y,[edellinen_suunta])[0]
            suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
            if self.suora_pakotettu_naapuri((x,y), edellinen_suunta):
                pisteet = self.kartta.hae_suunnat(x,y,self.hae_pakotetut_suorat_naapurit(edellinen_suunta))
                for piste in pisteet:
                    suunnat.append(self.hae_tulosuunta((x,y),piste[0]))
        return suunnat
    
    def hae_etaisyys(self, alku, loppu, suunta):
        etaisyys = 0
        matkaaja = alku
        while not matkaaja == loppu and etaisyys < 2*max(self.kartta.korkeus,self.kartta.leveys):
            etaisyys += 1
            matkaaja = (matkaaja[0]+suunta[0], matkaaja[1]+suunta[1])
        if 0 in suunta:
            return etaisyys
        return etaisyys*sqrt(2)
    
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
