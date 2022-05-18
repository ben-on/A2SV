class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        l,r=0,s
        if s-nums[0]!=0 :
            for i in range(1,len(nums)) :
                l+=nums[i-1]
                r=s-l-nums[i]
                if l==r :
                    return i
            return -1
        else :
            return 0