class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul1,mul2,lst=nums[0],nums[-1],[1]*len(nums)
        for i in range(1,len(nums)) :
            lst[i]=mul1
            mul1*=nums[i]
        for j in range(2,len(nums)+1) :
            lst[-j]*=mul2
            mul2*=nums[-j]
        return lst