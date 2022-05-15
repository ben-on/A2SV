# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=ListNode()
        head2=head1
        boo=False
        while list1 or list2 :
            boo=True
            if list1 and list2 and list1.val < list2.val:
                head1.val=list1.val
                head1.next=ListNode()
                head1=head1.next
                list1=list1.next
            elif list1 and list2 and list1.val >= list2.val:
                head1.val=list2.val
                head1.next=ListNode()
                head1=head1.next
                list2=list2.next
            elif list1 :
                head1.val=list1.val
                if list1.next :
                    head1.next=ListNode()
                    head1=head1.next
                list1=list1.next
            elif list2 :
                head1.val=list2.val
                if list2.next :
                    head1.next=ListNode()
                    head1=head1.next
                list2=list2.next
        if head2 and boo:
            return head2
        else :
            return None

                
                