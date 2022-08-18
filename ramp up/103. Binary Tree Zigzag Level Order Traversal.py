# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        qu=deque([root])
        ans=[[root.val]]
        b=True
        while qu:
            r=len(qu)
            level=[]
            for i in range(r):
                temp=qu.popleft()
                # print(temp.val)
                if temp.left:
                    qu.append(temp.left)
                    level.append(temp.left.val)
                if temp.right:
                    qu.append(temp.right)
                    level.append(temp.right.val)
            if level:
                if b:
                    ans.append(list(reversed(level)))
                    b=False
                else:
                    ans.append(level)
                    b=True
        return ans
                
                
            