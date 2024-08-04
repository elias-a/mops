

def metric_plus(entity_stats, parent_stats):
    obp, slg, _ = entity_stats
    parent_obp, parent_slg, _ = parent_stats
    return 100 * ((obp / parent_obp) + (slg / parent_slg) - 1)
