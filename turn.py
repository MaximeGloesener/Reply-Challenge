
class Game:
    """
    # Parameters
    TM = nombre minimum de building à alimenter \n
    TX = nombre max à alimenter \n
    TR = profit par building alimenté
    """
    def __init__(self, TM, TX, TR):
        self.TM = TM
        self.TX = TX
        self.TR = TR
        self.instantiated_resource = []
        self.resource_powered_multiplier = 1
        self.resource_multiplier = 1
        self.profit_multiplier = 1

    def buy_resources(self, ressource):
        ...

    def compute_score(self):
        buildings = 0
        for ressource in self.instantiated_resource:
            if ressource.is_active():
                buildings += ressource.RU

        if buildings < self.TM: return 0
        return min(buildings, self.TX) * self.TR
                