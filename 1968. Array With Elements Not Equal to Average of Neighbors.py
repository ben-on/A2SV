class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for j in range(15):
            for i in range(len(nums)-2):
                if (nums[i]+nums[i+2])/2==nums[i+1]:
                    nums[i+1],nums[i+2]=nums[i+2],nums[i+1]
            
        return nums
        