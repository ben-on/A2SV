class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        
        nums.sort()
        p1=0
        p2=len(nums)-1
        
        while(p1<p2) :
            if nums[p1]+nums[p2]==k :
                count+=1
                p1+=1
                p2-=1
            elif nums[p1]+nums[p2] < k :
                p1+=1
            elif nums[p1]+nums[p2] > k :
                p2-=1
        return count
                
    
#         for i in range(int(len(nums)/2)):
#             if nums[i]=="" :
#                 continue
#             for j in range(i+1,len(nums)):
#                 if nums[j]=="" :
#                     continue
#                 if nums[i]+nums[j]==k :
#                     count+=1
#                     nums[i]=""
#                     nums[j]=""
                    
#                     break
        
#         return count
                    
                