
class Resources:
    """
    # Parameters
    RI : id ressource \n
    RA : cost activation
    RP : cost maintenance
    RW : nombre de tours où la ressource est active et génère profit
    RM : nombre de tours où inactif
    RL : nombre de temps de vie total (ressource fait RW actif puis RM inactif en boucle)
    RU : nombre de building powered par la ressource
    RT : special effect
    RE : valeur special effect
    """
    def __init__(self, RI, RA, RP, RW, RM, RL, RU, RT, RE):
        self.RI = RI # id ressource
        self.RA = RA # cost activation
        self.RP = RP # cost maintenance
        self.RW = RW # nombre de tours où la ressource est active et génère profit
        self.RM = RM # nombre de tours où inactif
        self.RL = RL # nombre de temps de vie total (ressource fait RW actif puis RM inactif en boucle)
        self.RU = RU # nombre de building powered par la ressource
        self.RT = RT # special effect
        self.RE = RE

        self.turn = 0
        self.score = self.naive_score()

    def is_active(self):
        if self.turn >= self.RL:
            return False
        return (self.turn % (self.RM + self.RW)) < self.RW

    def forward(self):
        self.turn += 1

    def backward(self):
        self.turn -= 1

    def applyEffect(self, game):
        if not self.is_active():
            return
        if self.RE == "A":
            game.building_powered_multiplier += self.RE/100
            game.building_powered_multiplier = max(game.building_powered_multiplier, 0)
        elif self.RE == "B":
            game.building_multiplier += self.RE/100
            game.building_multiplier = max(game.building_multiplier, 0)
        elif self.RE == "C":
            game.life_multiplier += self.RE/100
        elif self.RE ==  "D":
            game.profit_multiplier += self.RE/100
            game.profit_mutliplier = max(game.profit_multiplier, 0)

    def naive_score(self):
        import random
        score = self.RU
        # score = (self.RU * self.RW) / (self.RA + self.RP * self.RL)
        # score *= (1 + abs(int(self.RE)) / 100) if self.RE else 1

        """
        if self.RT == "A" and int(self.RE) > 0:
            score*=2
        if self.RT == "D" and int(self.RE)>0:
            score*=2
        if self.RT == "E" and int(self.RE)>0:
            score*=2
        """
        return score
