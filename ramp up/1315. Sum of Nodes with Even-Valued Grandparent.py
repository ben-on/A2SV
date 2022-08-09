# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        #algorithm just preserve their parents in stack like [node,[parents.vaues]]
        stk=[[root,[]]]
        ans=0
        while stk:
            # print(stk)
            temp=stk.pop()
            try:
                if temp[1][-2]%2==0:
                    ans+=temp[0].val
            except:
                pass
            #print(temp[0].val,temp[1])
            new=[*temp[1],temp[0].val]
            if temp[0].left:
                stk.append([temp[0].left,new])
            if temp[0].right:
                stk.append([temp[0].right,new])
        return ans