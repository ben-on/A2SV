class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for i in range(len(position)) :
            t=(target-position[i])/speed[i]
            time.append(t)
        lst=[]
        for i in range(len(position)) :
            lst.append([position[i],time[i]])
        
        lst.sort()
        count=0
        temp=0
        for i in range(1,len(lst)+1) :
            if lst[-i][1] > temp :
                temp=lst[-i][1]
                count+=1
        return count
        
        
        
                
            
        