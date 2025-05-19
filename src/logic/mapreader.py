#Tulkitsee kartan muodon muille

dummykartta = "type octile\nheight 5 \nwidth 5\nmap\n@@@@@\n@...@\n@..@@ \n@...@ \n@@@@@"
COLORS = {
    "@":"black",
    ".":"white",
    "T":"gray",
    "*":"red"
}

def main():
    # TODO
    return

class asciiKartta:
    def __init__(self, kartta = dummykartta, pikselikoko = 10, colors = COLORS):
        karttalines = kartta.splitlines()
        self.korkeus = int(karttalines[1].split()[1])
        self.leveys = int(karttalines[2].split()[1])
        self.karttadata = karttalines[4:]
        self.varit = colors
        self.pikselikoko = pikselikoko

    def hae_vari(self,x,y):
        return self.varit[self.piste(x,y)]
    
    def piste(self,x,y):
        return self.karttadata[y][x]
    
    def vaihda_piste(self,x,y, char="*"):
        self.karttadata[y] = self.karttadata[y][:x] + char + self.karttadata[x + 1:]
        return 