from functools import partial
from mlb import Mlb


class Batter(Mlb):
    def __init__(self, id_, name, team_stats):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.team_stats = team_stats

    def mops_plus(self):
        stats = super().stats(partial(self.mlb.get_player_stats, self.id_))
        obp, slg, _ = stats
        team_obp, team_slg, _ = self.team_stats
        return 100 * ((obp / team_obp) + (slg / team_slg) - 1)

    def tabulate(self):
        return self.name, self.mops_plus()
