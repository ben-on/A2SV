class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        large=0
        for i in range(int(len(nums)/2)) :
            if nums[i] + nums[-i-1] > large :
                large = nums[i] + nums[-i-1]
        return large
            
        