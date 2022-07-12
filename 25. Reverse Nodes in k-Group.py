# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root=head
        stk=[]
        nroot=ListNode(0)
        copy=nroot
        while head:
            stk.append(head.val)
            if len(stk)==k:
                
                while stk:
                    nroot.next=ListNode(stk.pop())
                    nroot=nroot.next
                nroot.next=head.next
                head=nroot.next
            else :
                head=head.next
        return copy.next
                    
        