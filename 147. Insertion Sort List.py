# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head :
            lst.append(head.val)
            head=head.next
        lst.sort()
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next