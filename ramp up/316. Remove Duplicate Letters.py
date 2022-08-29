class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d=Counter(s)
        vis=set()
        stk=[]
        for i in s:
            if i not in vis:
                while stk and ord(stk[-1])>ord(i) and d[stk[-1]]>0:
                    vis.remove(stk[-1])
                    stk.pop()
                stk.append(i)
                vis.add(i)
                d[i]-=1
            else:
                d[i]-=1
        return "".join(stk)