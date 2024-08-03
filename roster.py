from team import Mariners


class MarinersBatters(Mariners):
    def __init__(self):
        super().__init__()

    def batters(self):
        return {p.id: p.fullname for p in self._filter()}

    def _roster(self):
        return self.mlb.get_team_roster(
            self.mariners_id(),
            rosterType="fullSeason",
            season=2024,
        )

    def _filter(self):
        return filter(self._is_batter, self._roster())

    def _is_batter(self, player):
        return player.primaryposition.type != "Pitcher"
