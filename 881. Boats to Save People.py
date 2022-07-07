class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,out,new=0,0,[]
        for k in people:
            if k >= limit:
                out+=1
            else:
                new.append(k)
        new.sort()
        j=len(new)-1
        while i < j:
            if new[i]+new[j] <= limit :
                i+=1
                j-=1
            else :
                j-=1
            out+=1
        if i==j:
            out+=1
        return out
        

        
                

            
                
            