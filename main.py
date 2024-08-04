from mariners import Mariners


mariners = Mariners()
team_stats = mariners.stats()
batters = mariners.batters()
[b.mops_plus() for b in batters]
print(mariners.tabulate(batters))
