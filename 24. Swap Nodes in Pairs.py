# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head :
            lst.append(head.val)
            head=head.next
        for i in range(0,len(lst)-1,2) :
            lst[i],lst[i+1]=lst[i+1],lst[i]
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next