from game import Game

class BaseEffect:
    def __init__(self):
        pass

class SmartMeter(BaseEffect):
    def __init__(self, value):
        self.value = value

    def apply(self, turn: Game):
        pass