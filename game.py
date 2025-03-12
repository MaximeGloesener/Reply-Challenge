from resources import Resources
class Game:
    """
    # Parameters
    TM = nombre minimum de building à alimenter \n
    TX = nombre max à alimenter \n
    TR = profit par building alimenté
    """
    def __init__(self, data_resource, D):
        self.TM = 0
        self.TX = 0
        self.TR = 0
        self.score_helper = [Resources(**data_resource[i]) for i in range(len(data_resource))]
        self.turn_instantiated_resource = []
        self.building_powered_multiplier = 1
        self.building_multiplier = 1
        self.profit_multiplier = 1
        self.life_multiplier = 1
        self.instantiated_resource = []
        self.data_resource = data_resource
        self.D = D
        self.save_dictionary = {}
        self.turn = -1

    def choose_ressources(self):
        # parcourir les ressources, tant qu'on a l'argent
        self.score_helper.sort(key= lambda x: x.score)
        buiding_alimentés = 0
        for ressource in self.score_helper:
            # si n building minimum ok: STOP
            if buiding_alimentés >= self.TM:
                break
            # si on a du budget
            if self.D >= ressource.RA:
                print('ON PREND LA RESSOURCE', ressource.RI)
                self.buy_resources(ressource.RI)
                buiding_alimentés += ressource.RU
                self.D -= ressource.RA


    def buy_resources(self, resource_id):
        resource_id -= 1
        current = Resources(**self.data_resource[resource_id])
        self.turn_instantiated_resource.append(current)
        self.instantiated_resource.append(current)
        self.save_dictionary.get(self.turn, []).append(resource_id+1)
        return current

    def compute_profit(self):
        # return profit au tour
        buildings = 0
        for ressource in self.instantiated_resource:
            if ressource.is_active():
                buildings += ressource.RU # si ressource active: get nbre building alimentés

        if buildings < self.TM: return 0
        return min(buildings, self.TX) * self.TR


    def compute_maintenance(self):
        # calcul des couts de maintenance
        maintenance = 0
        for ressource in self.instantiated_resource:
            if ressource.turn > 0 and ressource.turn < ressource.RL:
                maintenance += ressource.RP

        return maintenance

    # à chaque tour update état de la game: call à chaque tour
    def next_turn(self, TM, TX, TR):
        # mettre à jour ressources pour le prochain tour
        self.turn += 1
        for resource in self.instantiated_resource:
            resource.forward()
        self.TM = TM
        self.TX = TX
        self.TR = TR
        self.turn_instantiated_resource = []
        self.resource_powered_multiplier = 1
        self.resource_multiplier = 1
        self.profit_multiplier = 1

        # J'achète !
        self.save_dictionary[self.turn] = []
        self.choose_ressources()

        # calculer le profit du tour
        profit = self.compute_profit()

        # calculer les maintenances du tour
        maintenance = self.compute_maintenance()

        # mettre à jour le budget D (Ajout profit et Soustraire coûts de maintenance)
        self.D = self.D + profit - maintenance