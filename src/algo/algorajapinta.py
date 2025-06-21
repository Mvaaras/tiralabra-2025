class AlgoRajapinta:
    def __init__(self, algot):
        if not isinstance(algot, list):
            self.algot = [algot]
        else:
            self.algot = algot
        self.kohta = 0
        self.algo = self.algot[self.kohta]
        self.maara = len(self.algot)
        self.data = []

    def aloita_algo(self):
        return self.palauta_reitti(self.algo.aloita())
    
    def vaihda_alku(self, x,y=None):
        self.algo.vaihda_alku(x,y)

    def vaihda_loppu(self, x,y=None):
        self.algo.vaihda_loppu(x,y)

    def kartta(self):
        return self.algo.kartta
    
    def palauta_reitti(self,data):
        self.data = data
        if isinstance(data, list):
            return data
        return data["reitti"]
    
    def palauta_vieraillut(self):
        if isinstance(self.data, list):
            return []
        return self.data["vieraillut"]
    
    def palauta_pituus(self):
        if isinstance(self.data, list):
            return None
        return self.data["pituus"]
    
    def palauta_extra(self):
        if "hyppypisteet" in self.data:
            return self.data["hyppypisteet"]
        return []
    
    def vaihda_algo(self):
        self.kohta += 1
        if self.kohta >= self.maara:
            self.kohta = 0
        self.algo = self.algot[self.kohta]
        self.vaihda_alku(0,0)
        self.vaihda_loppu(0,0)

    def nimi(self):
        return self.algo.palauta_nimi()
