class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        vis,n,m=set([(0,0)]),len(grid),len(grid[0])
        hp=[[grid[0][0],0,0]]
        heapq.heapify(hp)
        moves=[(1,0),(0,1),(-1,0),(0,-1)]
        while hp:
            val,r,c=heapq.heappop(hp)
            if r==n-1 and c==m-1:
                return val
            for move in moves:
                tx=r+move[0]
                ty=c+move[1]
                if tx in range(n) and ty in range(m) and (tx,ty) not in vis:
                    vis.add((tx,ty))
                    heapq.heappush(hp,[max(val,grid[tx][ty]),tx,ty])
                    
                    