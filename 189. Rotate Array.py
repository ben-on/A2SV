class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stk=[0]*len(nums)
        for i in range(len(nums)) :
            stk[(i+k)%len(nums)]=nums[i]
        for j in range(len(nums)) :
            nums[j]=stk[j]
        