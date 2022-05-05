class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        lst=[]
        lst=sorted(arr,reverse=True)
        count=[]
        for i in range(len(arr)) :
            lst2=[]
            a=0
            a=arr.index(lst[i])
            b=arr[:a+1]
            count.append(len(b))
            
            for j in range(1,len(b)+1) :
                arr[j-1] = b[-j]
            lst2=arr[:len(arr)-i]
            
            count.append(len(lst2))
            for k in range(1,len(lst2)+1):
                arr[k-1] = lst2[-k]
            
        
        return count
                
                
            
            
            
        