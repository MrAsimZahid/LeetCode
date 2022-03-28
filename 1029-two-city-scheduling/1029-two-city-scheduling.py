class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs)//2
        minCost = 0
        for a, b in costs:
            refund.append(b - a)
            minCost += a
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost
        