# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        root=head
        l=0
        while head:
            l+=1
            head=head.next
        l2=0
        stk=[]
        mx=0
        while root:
            l2+=1
            if l2 > l//2:
                mx=max(stk.pop() + root.val,mx)
                root=root.next
            else:
                stk.append(root.val)
                root=root.next
        return mx
                