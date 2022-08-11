class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count=[1]*n
        ans=[0]*n
        if not edges:
            return [0]
        dic=defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        g=[dic[i] for i in range(n)]
        print(g)
        def postOrder(curr,parent):
            for it in g[curr]:
                if it!=parent:
                    postOrder(it,curr)
                    count[curr]+=count[it]
                    ans[curr]+=ans[it]+count[it]
            return
        def preOrder(curr,parent):
            for it in g[curr]:
                if it!=parent:
                    ans[it]=ans[curr]-count[it]+(n-count[it])
                    preOrder(it,curr)
            return
        postOrder(0,-1)
        preOrder(0,-1)
        return ans