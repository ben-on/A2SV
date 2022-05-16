# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head :
            lst.append(head.val)
            head=head.next
        d=Counter(lst)
        lst1=[]
        for i in d :
            if d[i]==1 :
                lst1.append(i)
        lst1.sort()
        cur = dummy = ListNode(0)
        for e in lst1:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
                