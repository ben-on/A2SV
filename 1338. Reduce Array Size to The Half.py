class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic={}
        val=[]
        leng=len(arr)
        a=0
        count=0
        for i in arr :
            if i in dic :
                dic[i]+=1
            else :
                dic[i]=1
        for j in dic :
            val.append(dic[j])  
        val.sort(reverse=True)
        print(dic,val)
        for k in val :
            if leng <= len(arr)/2 :
                break
            leng-=k
            count+=1

                
            
                
        return count

        