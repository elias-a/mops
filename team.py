from functools import partial
from mlb import Mlb
from batter import Batter


class Mariners(Mlb):
    def __init__(self, league):
        super().__init__()
        self.league = league
        self.id_ = self.get_id()

    def get_id(self):
        id_, *rest = self.mlb.get_team_id("Seattle Mariners")
        return id_

    def stats(self):
        return super().stats(partial(self.mlb.get_team_stats, self.id_))

    def batters(self):
        return (Batter(p.id, p.fullname, self, self.league) 
                for p in self._remove_pitchers())

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
