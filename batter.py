from functools import partial
from mlb import Mlb


class Batter(Mlb):
    def __init__(self, id_, name, team, league):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.team = team
        self.league = league

    def stats(self):
        stats = super().stats(partial(self.mlb.get_player_stats, self.id_))
        self.ops_plus = self.metric_plus(stats, self.league.stats())
        self.mops_plus = self.metric_plus(stats, self.team.stats())

    def metric_plus(self, stats, parent_stats):
        obp, slg, _ = stats
        parent_obp, parent_slg, _ = parent_stats
        return 100 * ((obp / parent_obp) + (slg / parent_slg) - 1)

    def tabulate(self):
        return self.name, self.ops_plus, self.mops_plus
