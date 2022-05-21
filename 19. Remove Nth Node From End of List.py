# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root,c ,c2= head ,0,0
        while head:
            head=head.next
            c+=1
        root2=root
        if c==n :
            return root.next
        if root == None :
            return None
        c=(c-n)
        while root :
            c2+=1
            if c2==c :
                root.next=root.next.next
                break
            root=root.next
        return root2
            