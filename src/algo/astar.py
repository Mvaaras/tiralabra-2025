#A* Algoritmin toteutus
from math import sqrt
from queue import PriorityQueue


class AStar:
    def __init__(self, alku, loppu, kartta):
        self.alku = alku
        self.loppu = loppu
        self.kartta = kartta
        self.edellinen = {alku:"alku"}
        self.lyhin_reitti_pisteeseen = {self.alku:0}
        self.jono = PriorityQueue()
        self.jono.put((self.minimietaisyys(self.alku),alku))
        self.jonossa = {alku:True}
        self.paras_potentiaalinen_reitti = {self.alku:self.minimietaisyys(self.alku)}

    def astar(self):

        while not self.jono.empty():
            tutkittava_koko = self.jono.get()
            tutkittava = tutkittava_koko[1]
            self.jonossa[tutkittava] = False
            x = tutkittava[0]
            y = tutkittava[1]
            if tutkittava == self.loppu:
                return self.palauta_reitti()

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
        print ("no route")

    def paivita_etaisyys(self, piste, naapuri, etaisyys):
        self.edellinen[piste] = naapuri
        self.lyhin_reitti_pisteeseen[piste] = etaisyys
        self.paras_potentiaalinen_reitti[piste] = etaisyys + self.minimietaisyys(piste)
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
        return sqrt(x_etaisyys**2+y_etaisyys**2)

    def palauta_reitti(self):
        reitti = []
        piste = self.loppu
        while piste != "alku":
            reitti.append(piste)
            piste = self.edellinen[piste]
        reitti.reverse()
        return reitti



