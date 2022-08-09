class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d={}
        for i in range(len(isConnected)):
            d[i]=[]
            for j in range(len(isConnected)):
                if i==j:
                    continue
                if isConnected[i][j]==1:
                    d[i].append(j)
        vis=set()
        ans=0
        for k in range(len(isConnected)):
            if k not in vis:
                ans+=1
                vis.add(k)
                stack=d[k]
                while stack:
                    temp=stack.pop()
                    vis.add(temp)
                    for child in d[temp]:
                        if child not in vis:
                            stack.append(child)
        return ans
                            