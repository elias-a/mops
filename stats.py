from dataclasses import dataclass, astuple


@dataclass(kw_only=True, frozen=True)
class Stats:
    obp: float
    slg: float
    ops: float

    def __iter__(self):
        return iter(astuple(self))
