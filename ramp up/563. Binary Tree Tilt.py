# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def allv(root):
            ret=[]
            stk=[root]
            while stk:
                temp=stk.pop()
                ret.append(temp)
                if temp.left:
                    stk.append(temp.left)
                if temp.right:
                    stk.append(temp.right)
            return ret
        def tilt(root):
            if root.left:
                left_sum=sum([i.val for i in allv(root.left)])
            else:
                left_sum=0
            if root.right:
                right_sum=sum([j.val for j in allv(root.right)])
            else :
                right_sum=0
            return abs(left_sum-right_sum)
        
        return sum([tilt(k) for k in allv(root)])
            
            
            