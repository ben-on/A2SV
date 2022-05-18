class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j,c=0,0
        while c < len(nums) and j < len(nums) :
            if nums[c]==0  :
                if nums[j]!=0 :
                    nums[c],nums[j]=nums[j],nums[c]
                    c+=1
                    j+=1
                else :
                    j+=1
            else :
                c+=1
                j+=1