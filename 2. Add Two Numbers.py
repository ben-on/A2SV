# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root1=l1
        root2=l2
        str1=""
        str2=""
        while root1 :
            str1+=str(root1.val)
            root1=root1.next
        while root2 :
            str2+=str(root2.val)
            root2=root2.next
        str3=""
        str4=""
        for i in range(1,len(str1)+1):
            str3+=str1[-i]
        for i in range(1,len(str2)+1):
            str4+=str2[-i]
        mysum=int(str3)+int(str4)
        lst=list(str(mysum))
        lst=reversed(lst)
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        
        
        
            
            