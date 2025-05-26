#Tulkitsee kartan muodon muille
from math import sqrt

DUMMYKARTTA = "type octile\nheight 5 \nwidth 5\nmap\n@@@@.\n....@\n@..@@\n@...@\n@.@@@"
OLETUSVARIT = {
    "@":"black",
    ".":"white",
    "T":"gray40",
    "*":"red"
}
VIRHE_PISTE_TYYPPI = "Yritettiin hakea koordinaatteja muilla kuin tuplella tai kahdella int"

def luo_polusta (polku=None, pikselikoko = 10, colors = None):
    if not polku:
        return AsciiKartta(DUMMYKARTTA, pikselikoko, colors)
    with open(polku, encoding="ascii") as f:
        kartta = f.read()
    f.close()
    return AsciiKartta(kartta, pikselikoko, colors)

class AsciiKartta:
    def __init__(self, kartta, pikselikoko, colors):
        #kartta-oliolle oleellinen tieto ja sen varsinainen luonti
        karttalines = kartta.splitlines()
        self.korkeus = int(karttalines[1].split()[1])
        self.leveys = int(karttalines[2].split()[1])
        self.karttadata = karttalines[4:]
        self.kartta_alkuperainen = self.karttadata.copy()

        #käyttöliittymän määritykset
        if colors is None:
            self.aseta_oletusvarit()
        else: self.varit = colors
        self.pikselikoko = pikselikoko

    #yleishyödylliset metodit.

    def piste(self,x,y=None):
        if y is None:
            if isinstance(x, tuple):
                return self._hae_piste(x[0],x[1])
            raise TypeError("(" + str(x) + "," + str(y) + ") - " + VIRHE_PISTE_TYYPPI)
        return self._hae_piste(x,y)

    def _hae_piste(self, x,y):
        return self.karttadata[y][x]

    def flush(self):
        self.karttadata = self.kartta_alkuperainen.copy()


    #reitinhaun hyödyntämät metodit - algoritmikäyttöön

    def hae_suunnat(self,x,y,suunnat=((0,-1,False),(1,0,False),(0,1,False),(-1,0,False),(1,-1,True),(1,1,True),(-1,1,True),(-1,-1,True))):
        # palauttaa kaikki suunnat joihin pisteestä x,y voi kulkea suoraan
        # listana jossa on uusien pisteiden koordinaatit ja matkojen pituudet (1 tai sqrt 2)
        palautetut_suunnat = []

        # tutkitaan suunnat
        for suunta in suunnat:
            tutkittava_piste = (x+suunta[0],y+suunta[1])
            if (-1 in tutkittava_piste or self.leveys == tutkittava_piste[0]
                or self.korkeus == tutkittava_piste[1]):
                continue
            if self.piste(tutkittava_piste) == ".":
                if suunta[2]:
                    palautetut_suunnat.append((tutkittava_piste,sqrt(2)))
                else:
                    palautetut_suunnat.append((tutkittava_piste,1))

        return palautetut_suunnat

    def vaihda_piste(self,x,y, char="*"):
        #vaihtaa pisteen arvon - oletuksena "*" jota käytetään vierailtuihin pisteisiin
        self.karttadata[y] = self.karttadata[y][:x] + char + self.karttadata[y][x + 1:]

    #käyttöliittymälle hyödylliset metodit

    def hae_vari(self,x,y):
        return self.varit[self.piste(x,y)]

    def aseta_oletusvarit(self):
        self.varit = OLETUSVARIT
