# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def check(node,target,maxi=False):
            stk,retf,ret,anss=[node],target,target,None
            while stk:
                temp=stk.pop()
                if maxi:
                    if temp.val > ret:
                        ret=temp.val
                        anss=temp
                else:
                    if temp.val < retf:
                        retf=temp.val
                        anss=temp
                if temp.left:
                    stk.append(temp.left)
                if temp.right:
                    stk.append(temp.right)
            return anss  
        stack=[root]
        while stack:
            temp=stack.pop()
            if temp.left and temp.right:
                erl=check(temp.left,temp.val,True)
                err=check(temp.right,temp.val)
                if err and erl:
                    erl.val,err.val=err.val,erl.val
                    break
            if temp.left:
                eror=check(temp.left,temp.val,True)
                if eror:
                    eror.val,temp.val=temp.val,eror.val
                    break
                stack.append(temp.left)
            if temp.right:
                eror=check(temp.right,temp.val)
                if eror:
                    eror.val,temp.val=temp.val,eror.val
                    break
                stack.append(temp.right)
                
            