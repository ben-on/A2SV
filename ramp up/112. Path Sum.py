# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #dfs
        if not root:
            return False
        stk=[[root,root.val]]
        while stk:
            temp=stk.pop()
            # print(temp)
            if temp[0].left:
                stk.append([temp[0].left,temp[1]+temp[0].left.val])
            if temp[0].right:
                stk.append([temp[0].right,temp[1]+temp[0].right.val])
            if not temp[0].left and not temp[0].right and temp[1]==targetSum:
                return True
        return False