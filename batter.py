from functools import partial
from mlb import Mlb
from batter_stats import metric_plus


class Batter(Mlb):
    def __init__(self, id_, name, team, league):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.team = team
        self.league = league

    def stats(self):
        stats = super().stats(partial(self.mlb.get_player_stats, self.id_))
        self.ops_plus = metric_plus(stats, self.league.stats())
        self.mops_plus = metric_plus(stats, self.team.stats())

    def tabulate(self):
        return self.name, self.ops_plus, self.mops_plus
