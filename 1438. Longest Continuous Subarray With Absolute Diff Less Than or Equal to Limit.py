class Solution(object):
    def longestSubarray(self, nums, limit):
        mini=deque([])
        maxi=deque([])
        st=0
        mxLen=0
        for i in range(len(nums)):
            while maxi and maxi[-1] < nums[i]:
                maxi.pop()
            maxi.append(nums[i])
            while mini and mini[-1] > nums[i]:
                mini.pop()
            mini.append(nums[i])
            if maxi[0]-mini[0] <=limit:
                mxLen=max(mxLen,i-st+1)
            else :
                if maxi[0]==nums[st]:
                    maxi.popleft()
                if mini[0]==nums[st]:
                    mini.popleft()
                st+=1
            
        return mxLen
            
            
