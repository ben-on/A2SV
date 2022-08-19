class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        qu=deque([])
        target=[]
        # print(target)
        for i in range(len(grid)):
            t=[]
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    t.append(2)
                    qu.append([i,j])
                elif grid[i][j]==1:
                    t.append(2)
                else:
                    t.append(0)
            target.append(t)
         
        rw,c=len(grid),len(grid[0])
        vis=set()
        ans=0
        # print(grid)
        while qu:
            r=len(qu)
            # print(qu)
            for i in range(r):
                temp=qu.popleft()
                moves=[(0,1),(1,0),(0,-1),(-1,0)]
                for move in moves:
                    zr=temp[0]+move[0]
                    on=temp[1]+move[1]
                    # print([zr,on])
                    if zr in range(rw) and on in range(c):
                        # print("condi",grid[zr][on])
                        if grid[zr][on]==1 and (zr,on) not in vis:
                            # print("something")
                            grid[zr][on]=2
                            vis.add((zr,on))
                            qu.append([zr,on])
            if qu:
                ans+=1
        return ans if grid==target else -1 
                
                    
            