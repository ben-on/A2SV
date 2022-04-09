class Solution:
    def sortSentence(self, s: str) -> str:
        result =s.split()
        print(result)
        order=[""]*len(result)
        for i in result:
            order[int(i[-1])-1]=i[:-1]
        
        return ' '.join(order)
        