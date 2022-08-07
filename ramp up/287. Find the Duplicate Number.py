class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #binary search
        left = 0
        right = len(nums) - 1
        while left < right:
            
            mid = (left + right) // 2
            
            count = sum(i <= mid for i in nums)
            # print("mid",mid,"count",count)
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return right
    
    
        #brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j==i:
        #             continue
        #         if nums[i]==nums[j]:
        #             return nums[i]
        
        