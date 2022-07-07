class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=mx=i=0
        for j in range(len(nums)):
            if nums[j]==0 :
                if zeros < k:
                    zeros+=1
                else :
                    while nums[i]!=0:
                        i+=1
                    i+=1
            mx=max(mx,j-i+1)
        return mx