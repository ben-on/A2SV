class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)) :
            if s[i] == "]" :
                l,n=[],[]
                while stk[-1]!="[" :
                    l.append(stk.pop())
                stk.pop()
                while stk and stk[-1].isdigit() :
                    n.append(stk.pop())
                myint=int("".join(reversed(n)))
                stk.append("".join(reversed(l))*myint)
            else :
                stk.append(s[i])
        fin="".join(stk)
        return fin
                
                
            
        