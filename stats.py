from roster import MarinersBatters


class Stats(MarinersBatters):
    def __init__(self):
        super().__init__()

    def tabulate(self):
        name_ops = zip(self.batters().values(), self.ops().values())
        return sorted(
            [[name, ops] for name, ops in name_ops],
            key=self._tabulate_key,
            reverse=True,
        )

    def ops(self):
        return {id_: self._ops(id_) for id_ in self.batters().keys()}

    def _ops(self, player):
        return self._select_split(self._splits(player)).stat.ops

    def _splits(self, player):
        stats = self.mlb.get_player_stats(
            player,
            ["season", "seasonAdvanced"],
            ["hitting"],
            **{"season": 2024},
        )
        return stats["hitting"]["season"].splits

    def _select_split(self, splits):
        season, *rest = splits
        if len(rest) == 0:
            return season
        return max([season] + rest, key=self._max_games_played)

    def _max_games_played(self, split):
        return split.stat.gamesplayed

    def _tabulate_key(self, row):
        return row[1]
