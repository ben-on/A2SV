class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lbool=[]
        
        for i in range(len(l)) :
            temp=[]
            
            tb=True
            temp=nums[l[i] : r[i]+1]
            temp.sort()
            d=temp[1] - temp[0]
            
            for j in range(1,len(temp)) :
                if temp[j]-temp[j-1] != d :
                    tb=False
    
            lbool.append(tb)
                
        return lbool
           

                                        
                                         
                                        
                                         
                            
