class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left <=right:
            mid = (left+right)//2
            if sum(((elem-1)//mid)+1 for elem in nums) > threshold:
                left = mid+1
            else :
                right= mid-1
        return left