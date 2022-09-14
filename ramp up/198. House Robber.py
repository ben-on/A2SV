class Solution:
    dp={}
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def calc(ind,va=0):
            if ind+2>=len(nums):
                return nums[ind]
            return va+max([calc(elem,nums[elem]) for elem in range(ind+2,len(nums))])
        return calc(-2)