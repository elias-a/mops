from dataclasses import dataclass


@dataclass
class Split:
    func: any

    def split(self):
        return self._select_split(self._get_splits())

    def _select_split(self, splits):
        season, *rest = splits
        if len(rest) == 0:
            return season
        return max([season] + rest, key=self._max_games_played)

    def _max_games_played(self, split):
        return split.stat.gamesplayed

    def _get_splits(self):
        stats = self.func(
            # TODO: Only need one of these.
            ["season", "seasonAdvanced"],
            ["hitting"],
            **{"season": 2024},
        )
        return stats["hitting"]["season"].splits
