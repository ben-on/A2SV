class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped,stk,pushed=list(reversed(popped)),[],list(reversed(pushed))
        while pushed :
            stk.append(pushed.pop())
            while stk and stk[-1]==popped[-1] :
                stk.pop()
                popped.pop()
        return len(popped)==0