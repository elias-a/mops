from league import League
from team import Mariners


league = League()
league_stats = league.stats()
mariners = Mariners(league)
team_stats = mariners.stats()
batters = mariners.batters()
[b.stats() for b in batters]
print(mariners.tabulate(batters))
