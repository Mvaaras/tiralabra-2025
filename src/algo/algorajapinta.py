class AlgoRajapinta:
    def __init__(self, algo):
        self.algo = algo
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
    
    def palauta_extra(self):
        if "hyppypisteet" in self.data:
            return self.data["hyppypisteet"]
        return []