class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(sr,sc,color=0):
            stk=[(sr,sc)]
            visited=set()
            goal=grid[sr][sc]
            while stk:
                temp=stk.pop()
                visited.add(temp)
                grid[temp[0]][temp[1]]=color
                ways=[(temp[0],temp[1]+1),(temp[0]+1,temp[1]),(temp[0],temp[1]-1),(temp[0]-1,temp[1])]
                for pair in ways:
                    if pair[0] in range(len(grid)) and pair[1] in range(len(grid[0])):
                        if grid[pair[0]][pair[1]]==goal and pair not in visited:
                            stk.append(pair)
           
            return len(visited)
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,check(i,j))
        return ans