class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens :
            if i =="+":
                temp=stk.pop()
                temp2=stk.pop()
                stk.append(temp2+temp)
            elif i=="-":
                temp=stk.pop()
                temp2=stk.pop()
                stk.append(temp2-temp)
                
            elif i=="/":
                temp=stk.pop()
                temp2=stk.pop()
                temp3=temp2/temp
                stk.append(int(temp3))
            elif i=="*":
                temp=stk.pop()
                temp2=stk.pop()
                stk.append(temp2*temp)
            else :
                stk.append(int(i))
            
        return stk[0]

        