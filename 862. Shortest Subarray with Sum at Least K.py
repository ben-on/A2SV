class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que, mini = deque(), len(nums)+1
        pre_sum =[0]
        for i in nums :
            pre_sum.append(pre_sum[-1]+i)
        for i, n in enumerate(pre_sum):
            while que and pre_sum[que[-1]] >= n:
                que.pop()
            while que and n - pre_sum[que[0]] >= k:
                mini = min(mini, i - que.popleft())
            que += i,
        return mini if mini != len(nums)+1 else -1
        
        
        
        
#         lst=[]
#         mini=len(nums)
#         check=0
#         for i in range(len(nums)):
#             s=0
#             for j in range(i,len(nums)):
#                 s+=nums[j]
#                 if s >=k:
#                     check+=1
#                     if j+1-i<mini:
#                         mini=j+1-i
#                     break
#         if check>0:
#             return mini
#         return -1
       
        
            