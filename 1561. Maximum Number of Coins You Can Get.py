class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        
        count=0
        myint=0
        for i in range(1,len(piles),2):
            if count == len(piles)/3 :
                break

            myint+=piles[i]
            count+=1
            
        return myint
        