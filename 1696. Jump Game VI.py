class Solution:
    def maxResult(self, nums, k):
        ans = [(0,-k)]

        for i in range(len(nums)):
            while i - ans[0][1] > k:
                heappop(ans)

            nums[i] -= ans[0][0]

            heapq.heappush(ans, (-nums[i],i))

        return nums[-1]
 





#     def maxResult(self, nums: List[int], k: int) -> int:
#         count=0
#         score=nums[0]
#         # print(score)
#         neg=[-float('inf'),0]
#         i=1
#         while i < len(nums):
#             count+=1
#             if nums[i] <= 0:
#                 if i==len(nums)-1:
#                     score+=nums[i]
#                     # print(score,i)
#                     break
#                 # neg[0]=max(nums[i],neg[0])
#                 if nums[i] > neg[0]:
#                     neg[1]=i
#                     neg[0]=nums[i]
#             if nums[i]  > 0:
#                 score+=nums[i]
#                 # print(score,i)
#                 count=0
#             if count ==k:
#                 score+=neg[0]
#                 while i != neg[1]:
#                     i-=1
#                 # print(score,i)
#                 neg[0]=-float('inf')
#                 count=0
#             i+=1
#         return score
                