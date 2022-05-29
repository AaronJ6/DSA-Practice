def mincostTickets(self, days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """    
    total_costs = [0] * len(days)
    
    t7 = t30 = 0        
    for i, day in enumerate(days):
        while day - days[t7] >= 7:
            t7 += 1
        while day - days[t30] >= 30:
            t30 += 1
            
        total_costs[i] = min(total_costs[i-1] + costs[0], 
                            total_costs[t7-1] + costs[1],
                            total_costs[t30-1] + costs[2])
    return total_costs[-1]