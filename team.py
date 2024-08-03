from mlb import Mlb


class Mariners(Mlb):
    def __init__(self):
        super().__init__()

    def mariners_id(self):
        id_, *rest = self.mlb.get_team_id("Seattle Mariners")
        return id_

    def ops(self):
        stats = self.mlb.get_team_stats(
            self.mariners_id(),
            ["season", "seasonAdvanced"],
            ["hitting"],
            **{"season": 2024},
        )
        split, *rest = stats["hitting"]["season"].splits
        return split.stat.ops
