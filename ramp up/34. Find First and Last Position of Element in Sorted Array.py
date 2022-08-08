class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        ans=[-1,-1]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left = mid +1
            elif nums[mid]>target:
                right= mid -1
            else:
                ans=[mid,mid]
                break
        while nums and ans[1]<len(nums)-1 and nums[ans[1]+1]==target :
            ans[1]+=1
        while ans[0] >0 and nums and nums[ans[0]-1]==target:
            ans[0]-=1 
        return ans