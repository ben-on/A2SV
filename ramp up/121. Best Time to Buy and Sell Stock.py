class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mm=prices[0]
        res=0
        for i in prices:
            res = max(res,i-mm)
            mm = min(mm,i)
        return res