class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp,r,c={},len(grid)-1,len(grid[0])-1
        def dynamic(n,m):
            if n==0 and m==0:
                return grid[0][0]
            if (n,m) in dp:
                return dp[(n,m)]
            if n==0:
                dp[(n,m)] = grid[n][m]+dynamic(n,m-1)
            elif m==0:
                dp[(n,m)] = grid[n][m]+dynamic(n-1,m)
            else: 
                dp[(n,m)] = grid[n][m]+min(dynamic(n-1,m),dynamic(n,m-1))
            return dp[(n,m)]
        return dynamic(r,c)