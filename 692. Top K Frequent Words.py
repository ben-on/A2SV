class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        new=Counter(words)
        lst=[[-new[i],i] for i in new]
        heapq.heapify(lst)
        return [heapq.heappop(lst)[1] for _ in range(k)]