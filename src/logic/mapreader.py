#Tulkitsee kartan muodon muille
from math import sqrt

dummykartta = "type octile\nheight 5 \nwidth 5\nmap\n@@@@@\n@...@\n@..@@ \n@...@ \n@@@@@"
COLORS = {
    "@":"black",
    ".":"white",
    "T":"gray36",
    "*":"red"
}

def luo_polusta (polku=None, pikselikoko = 10, colors = COLORS):
    if not (polku):
        return asciiKartta(dummykartta, pikselikoko, colors)
    with open(polku) as f:
        kartta = f.read()
    f.close()
    return asciiKartta(kartta, pikselikoko, colors)

class asciiKartta:
    def __init__(self, kartta, pikselikoko, colors):
        #kartta-oliolle oleellinen tieto ja sen varsinainen luonti
        karttalines = kartta.splitlines()
        self.korkeus = int(karttalines[1].split()[1])
        self.leveys = int(karttalines[2].split()[1])
        self.karttadata = karttalines[4:]

        #käyttöliittymän määritykset
        self.varit = colors
        self.pikselikoko = pikselikoko
    
    #yleishyödylliset metodit.

    def piste(self,x,y=None):
        if y == None:
            if type(x) == tuple:
                return self._hae_piste(x[0],x[1])
            else: raise TypeError("(" + str(x) + "," + str(y) + ") - Yritettiin hakea koordinaatteja muilla kuin tuplella tai kahdella int")
        else:
            return self._hae_piste(x,y)

    def _hae_piste(self, x,y):
        return self.karttadata[y][x]

    
    #reitinhaun hyödyntämät metodit - algoritmikäyttöön

    def hae_suunnat(self,x,y):
        # palauttaa kaikki suunnat joihin pisteestä x,y voi kulkea suoraan listana jossa on uusien pisteiden koordinaatit ja matkojen pituudet (1 tai sqrt 2)
        suunnat = []

        # suorat järjestyksessä u r d l
        for suunta in ((0,-1),(1,0),(0,1),(-1,0)):
            tutkittava_piste = (x-suunta[0],y-suunta[1])
            if -1 in tutkittava_piste or self.leveys == tutkittava_piste[0] or self.korkeus == tutkittava_piste[1]:
                continue
            elif self.piste(tutkittava_piste) == ".":
                suunnat.append(tutkittava_piste,1)

        # kulmittaiset ur dr dl ul
        for suunta in ((1,-1),(1,1),(-1,1),(-1,-1)):
            tutkittava_piste = (x-suunta[0],y-suunta[1])
            if -1 in tutkittava_piste or self.leveys == tutkittava_piste[0] or self.korkeus == tutkittava_piste[1]:
                continue
            elif self.piste(tutkittava_piste[0],tutkittava_piste[1]) == ".":
                suunnat.append(tutkittava_piste,sqrt(2))
        
        return suunnat

    def vaihda_piste(self,x,y, char="*"):
        #vaihtaa pisteen arvon - oletuksena "*" jota käytetään vierailtuihin pisteisiin
        self.karttadata[y] = self.karttadata[y][:x] + char + self.karttadata[x + 1:]
        return 
    
    #käyttöliittymälle hyödylliset metodit

    def hae_vari(self,x,y):
        return self.varit[self.piste(x,y)]