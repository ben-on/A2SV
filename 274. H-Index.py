class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count=0
        for i in range(len(citations)) :
            if citations[i] >i :
                count+=1
        return count
            