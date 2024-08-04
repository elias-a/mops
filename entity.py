import mlbstatsapi
from split import Split


class MlbEntity:
    def __init__(self):
        self.mlb = mlbstatsapi.Mlb()

    def ops(self, func, id_):
        split = Split(func, id_)
        return split.split().stat.ops
