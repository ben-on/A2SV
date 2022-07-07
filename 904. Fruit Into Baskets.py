class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        for k in range(1,len(fruits)) :
            if fruits[i]!=fruits[k]:
                j=k
                break
        
        lst=[fruits[i],fruits[j]]
        ans=j-i+1
        mx=ans
        
        # print(ans)
        # print(lst)
        for i in range(j+1,len(fruits)):
            if fruits[i] in lst:
                ans+=1
                continue
            else :
                # print("previous length :",ans)
                
                if ans >mx:
                    # print("condition satisfied")
                    mx=ans
                temp=fruits[i-1]
                
                # print("temp: ",temp)
                
                point=i-1
                while point >=0 and fruits[point-1] == temp:
                    point-=1
                    
                # print("changed point: ", point)
                
                lst=[fruits[point],fruits[i]]
                
                # print("new arr : ",lst)
                
                ans=i-point+1
                
                # print("new length: ",ans)
                
        # print("last value: ",ans)
        if ans >mx:
            mx=ans
        return mx
                    
        