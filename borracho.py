import random

class Borracho:

    def __init__(self, nombre):
        self.name = nombre

class  borrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        sig_paso = [(0,1), (0,-1), (1,0),(-1,0)]
        d = random.choices(range(len(sig_paso)),weights=(25,25,25,25),k=1)
        dint = int(d[0])
        return sig_paso[dint]
        