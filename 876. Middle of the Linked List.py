# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=head
        count=0
        while root:
            count+=1
            root=root.next
        for i in range(int(count/2)):
            head=head.next
        return head
       