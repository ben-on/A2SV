class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        #brute force
        # t=1
        # while totalTrips:
        #     for i in time:
        #         if totalTrips==0:
        #             return t
        #         if t%i==0:
        #             totalTrips-=1
        #     t+=1
        # return t-1
        # print(totalTrips)
        # return t
        left,right=0,max(time)*totalTrips
        while left <=right:
            mid=(left+right)//2
            if sum([mid//i for i in time]) < totalTrips:
                left = mid+1
            else :
                right = mid-1
        return right
                
                
        