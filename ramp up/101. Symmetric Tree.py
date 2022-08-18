# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qu=deque([root])
        
        boo=True
        while qu:
            left=[]
            rang=len(qu)
            for i in range(rang):
                child=qu.popleft()
                if child.left:
                    qu.append(child.left)
                    left.append(child.left.val)
                else :
                    left.append('none')
                if child.right:
                    qu.append(child.right)
                    left.append(child.right.val)
                else :
                    left.append('none')
            if len(qu)!=0:
                a=int((len(left)/2))
                print(left)
                oneLeft=left[:a]
                twoLeft=left[a:]
                four=[]
                
                for i in range(1,len(twoLeft)+1):
                    four.append(twoLeft[-i])
                if four!=oneLeft:
                    boo=False
        return boo
        