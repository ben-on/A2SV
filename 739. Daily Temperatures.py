class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst=[]
        out=[0]*len(temperatures)
        
        
        for idx,elem in enumerate(temperatures):
            
            while len(lst)>0 and elem > temperatures[lst[-1]] :
                
                new=lst.pop()
                out[new]=idx-new
            lst.append(idx)
            
        return out
    
    
    
    
#         for i in range(len(temperatures)):
#             if temperatures[i] <= lst[-1][0] :
#                 lst.append([temperatures[i],i])
#             elif temperatures[i] > lst[-1][0] :
#                 while  temperatures[i] > lst[-1][0]:
#                     out.append(i-lst[-1][1])
#                     lst.pop()
                
#         return out
                    
        
        
        
        
        # out=[0]*len(temperatures)
        # for i in range(len(temperatures)-1) :
        #     count=0
        #     boo=False
        #     for j in range(i+1,len(temperatures)) : 
        #         if temperatures[j] > temperatures[i] :
        #             count+=1
        #             boo=True
        #             break
        #         elif temperatures[j] <= temperatures[i]:
        #             count+=1
        #     if count >0 and boo :
        #         out[i]=count
        # return out
