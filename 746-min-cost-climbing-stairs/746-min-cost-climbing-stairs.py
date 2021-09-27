class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # runningMinCosts = [0] * len(cost)
        
        c1, c2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            c = min(c1, c2) + cost[i]
            c1, c2 = c2, c
        return(c2)
        