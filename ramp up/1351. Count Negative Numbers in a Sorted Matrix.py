class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0  
        for i in grid:
            beg = 0 
            end = len(i) - 1
            
            while beg <= end:
                print(i[beg],i[end])
                mid = (beg+end)//2
                if i[mid] < 0:
                    end = mid - 1
                elif i[mid] >= 0:
                    beg = mid + 1
            res += (len(i)  - beg)
        return res