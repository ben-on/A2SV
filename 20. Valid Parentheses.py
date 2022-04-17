class Solution:
    def isValid(self, s: str) -> bool:
        boo=True
        d={"(":")","[":"]","{":"}"}
        lst=[]
        for i in s:
            if i in d:
                lst.append(i)
            elif len(lst)>0 and d[lst[-1]]==i:
                lst.pop()
            else:
                boo=False
                break
        if len(lst)==0:
            return boo
        else:
            return False
                
            
                
                
        
        
        
        
        
        
        
        
        
        
        
    