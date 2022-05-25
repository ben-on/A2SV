class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        qu = deque()
        for i in matrix :
            qu.append(deque(i))
        lst=[]
        while qu :
            t=[]
            t1=[]
            for i in range(1,len(qu)-1) :
                if not qu[i] :
                    continue
                if qu[i] :
                    t1.append(qu[i].pop())
                if qu[i] :
                    t.append(qu[i].popleft())
            if len(qu) > 2 :
                lst=[*lst,*list(qu.popleft()),*t1,*reversed(list(qu.pop())),*reversed(t)]
            elif len(qu) ==2 :
                lst=[*lst,*list(qu.popleft()),*reversed(list(qu.pop()))]
            else :
                lst=[*lst,*list(qu.popleft())]
        return lst
                
        
            
            
    
                
                
                
                
                
            