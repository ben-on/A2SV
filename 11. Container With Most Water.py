class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        mxm=(j-i)*min(height[j],height[i])
        while i < j :
            if mxm < (j-i)*min(height[j],height[i]) :
                mxm = (j-i)*min(height[j],height[i])
            if height[j] <= height[i] :
                j-=1
            else :
                i+=1
        return mxm
            
        