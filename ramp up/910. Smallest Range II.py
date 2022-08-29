class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        gap=nums[-1]-nums[0]
        n=len(nums)
        for i in range(n-1):
            high=max(nums[n-1]-k,nums[i]+k)
            low=min(nums[0]+k,nums[i+1]-k)
            gap=min(gap,high-low)
        return gap if gap!=float('inf') else 0
            
        