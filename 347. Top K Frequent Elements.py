class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        val = []
        fin=[]
        for i in nums :
            if i in dic :
                dic[i]+=1
            else :
                dic[i]=1
        for i in dic :
            val.append([dic[i],i])
        val.sort(reverse=True)
        for i in range(k) :
            fin.append(val[i][1])
        return fin
        
