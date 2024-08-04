from mlb import Mlb


class League(Mlb):
    def __init__(self):
        super().__init__()

    def stats(self):
        return super().stats(self.mlb.get_stats)
