# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        root1,root2,root3,c1,c2,c3,lst1,lst2=head,head,head,0,0,0,[],[]
        
        while root1 :
            c1+=1
            root1=root1.next
        while root2 :
            c2+=1
            if c2 > c1//2 :
                lst2.append(root2)
            else :
                lst1.append(root2)
            root2=root2.next
        lst1.reverse()
        if lst1 :
            lst1.pop()
        while lst1 or lst2 :
            if c3%2==0 and lst1 :
                root3.next=lst1.pop()
            elif lst2 :
                root3.next=lst2.pop()
            root3=root3.next
            c3+=1
        root3.next=None
        