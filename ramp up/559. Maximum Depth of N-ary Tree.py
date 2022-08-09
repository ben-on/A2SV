"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        try:
            stk=[[root,1]]
            ans=0
            while stk:
                temp=stk.pop()
                ans=max(ans,temp[1])
                for i in temp[0].children:
                    stk.append([i,temp[1]+1])
            return ans
        except:
            return 0