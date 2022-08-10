# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return root
        stk=[[-1,root,[]]]
        hp=[]
        dic={}
        heapq.heapify(hp)
        while stk:
            temp=stk.pop()
            dic[temp[1].val]=temp[1]
            heapq.heappush(hp,[temp[0],temp[1].val,temp[2]])
            new=[*temp[2],temp[1].val]
            if temp[1].left:
                stk.append([temp[0]-1,temp[1].left,new])
            if temp[1].right:
                stk.append([temp[0]-1,temp[1].right,new])
        ans=[heapq.heappop(hp)]
        while hp[0][0]==ans[-1][0]:
            ans.append(heapq.heappop(hp))
            ans[-1][2]=set(ans[-1][2])
        if len(ans)==1:
            return dic[ans[0][1]]
        for i in range(-1,-len(ans[0][2])-1,-1):
            b=True
            for j in range(1,len(ans)):
                if ans[0][-1][i] not in ans[j][-1]:
                    b=False
            if b:
                return dic[ans[0][-1][i]]
        return dic[ans[0][-1][-1]]
                
        

