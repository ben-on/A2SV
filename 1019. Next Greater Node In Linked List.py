# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack,count,answer=[],0,[]
        while head:
            answer.append(0)
            while stack and head.val > stack[-1][0]:
                temp = stack.pop()
                answer[temp[1]] = head.val
            stack.append([head.val,count])
            count+=1
            head=head.next
            
        return answer