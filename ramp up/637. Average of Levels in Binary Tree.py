# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        qu, arr = deque([root]), [root.val]
        while qu:
            rang=len(qu)
            c=0
            for i in range(rang):
                child=qu.popleft()
                if child.left:
                    qu.append(child.left)
                    c+=child.left.val
                    
                if child.right:
                    qu.append(child.right)
                    c+=child.right.val
            if len(qu) >  0:      
                av=c/len(qu)
                arr.append(av)
        return arr