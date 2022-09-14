class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp={}
        def dynamic(col,row):
            if row==len(triangle)-1:
                return triangle[row][col]
            if (col,row) in dp:
                return dp[(col,row)]
            dp[(col,row)]=triangle[row][col]+min(dynamic(col,row+1),dynamic(col+1,row+1))
            return dp[(col,row)]
        return dynamic(0,0)