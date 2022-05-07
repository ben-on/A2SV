class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        for i in s :
            if i=="(" or i!=")" :
                stk.append(i)
            elif i==")" :
                temp=[]
                while stk[-1] != "(" :
                    
                    temp.append(stk.pop())
                stk.pop()
                for i in temp :
                    stk.append(i)
        fin=""
        for i in stk :
            fin+=i
        return fin
                    
                    
        
        
        
        
        
#         lst=[]
#         for i in s :
#             lst.append(i)
        
#         cl=[[0,'']]
#         op=[[0,'']]
#         for i in range(len(lst)) :
#             if cl[0][1]==')' and op[0][1] =='(' :
#                 a=cl[0][0]
#                 b=op[0][0]
                
#                 temp=lst[b+1:a]
                
#                 print(a,b)
#                 count=0
#                 for k in range(a,a+len(temp)) :
#                     if temp[count]=='(' :
#                         temp[count]=')'
#                     if temp[count]==')' :
#                         temp[count]='('
#                     lst[k] = temp[count]
#                     count+=1
#                 cl[0][0]=0
#                 cl[0][1]=''
#                 op[0][0]=0
#                 op[0][1]=''
                
                
#             else :
#                 if lst[i]=='(' :
#                     op[0][0]=i
#                     op[0][1]='('

#                 if lst[-i-1] == ')' :
#                     cl[0][0] = -i-1
#                     cl[0][1] = ')'
#         print(lst)
                
            
                

                

            
                
        
        
                    