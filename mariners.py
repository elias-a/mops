from tabulate import tabulate
from functools import partial
from mlb import Mlb
from batter import Batter


class Mariners(Mlb):
    def __init__(self):
        super().__init__()
        self.id_ = self.get_id()

    def tabulate(self, batters):
        sorted_batters = sorted(batters, key=self._tabulate_key, reverse=True)
        return tabulate(b.tabulate() for b in sorted_batters)

    def _tabulate_key(self, batter):
        return batter.mops_plus()

    def get_id(self):
        id_, *rest = self.mlb.get_team_id("Seattle Mariners")
        return id_

    def stats(self):
        return super().stats(partial(self.mlb.get_team_stats, self.id_))

    def batters(self):
        return [Batter(p.id, p.fullname, self.stats())
                for p in self._remove_pitchers()]

    def _roster(self):
        return self.mlb.get_team_roster(
            self.id_,
            rosterType="fullSeason",
            season=2024,
        )

    def _remove_pitchers(self):
        return filter(self._is_batter, self._roster())

    def _is_batter(self, player):
        return player.primaryposition.type != "Pitcher"
