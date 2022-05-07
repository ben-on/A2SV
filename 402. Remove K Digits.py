class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        for i in range(len(num)):
            while stk and k>0 and stk[-1] > int(num[i]) :
                stk.pop()
                k-=1
            stk.append(int(num[i]))
        fin = ''
        if k!=0 :
            for j in range(k):
                stk.pop()
        for i in stk :
            fin+=str(i)
        
        if stk :
            return str(int(fin))
        return "0"
            
        
            