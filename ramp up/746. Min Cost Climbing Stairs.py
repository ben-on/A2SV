class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def check(idx):
            if idx>len(cost)-1:
                return 0
            if idx in dp:
                return dp[idx]
            dp[idx]=cost[idx]+min(check(idx+1),check(idx+2))
            return dp[idx]
        return min(check(0),check(1))