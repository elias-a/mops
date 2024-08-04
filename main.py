from tabulate import tabulate
from league import League
from team import Mariners


league = League()
league_stats = league.stats()
mariners = Mariners(league)
team_stats = mariners.stats()
batters = mariners.batters()
[b.stats() for b in batters]
[print(b) for b in batters]
print(tabulate([b.tabulate() for b in batters]))
