class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                s=str(nums[j])+str(nums[j+1])
                t=str(nums[j+1])+str(nums[j])
                if int(s)<int(t):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        fs=""
        for i in nums:
            fs+=str(i)
        if int(fs)==0:
            return "0"
        else:
            return fs