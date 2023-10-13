class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        min_cost = [0] * (n + 1)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        
        for i in range(2, n):
            min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + cost[i]
        return min(min_cost[n - 1], min_cost[n - 2])