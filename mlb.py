import mlbstatsapi
from split import Split
from stats import Stats


class Mlb:
    def __init__(self):
        self.mlb = mlbstatsapi.Mlb()

    def stats(self, func):
        split = Split(func)
        stats = split.split().stat
        obp, slg, ops = [float(s) for s in [stats.obp, stats.slg, stats.ops]]
        return Stats(obp=obp, slg=slg, ops=ops)
