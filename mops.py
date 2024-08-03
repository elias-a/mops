from team import Mariners
from roster import MarinersBatters


class MOPS:
    def __init__(self):
        self.mariners = Mariners()
        self.batters = MarinersBatters()

    def mops(self):
        return {id_: self._mops(id_) for id_ in self.batters.batters().keys()}

    def _mops(self, player):
        return 100 * (self.batters.ops() / self.mariners.ops() - 1)
