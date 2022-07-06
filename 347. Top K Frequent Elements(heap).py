class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        frq=Counter(nums)
        lst=[[-frq[i],i] for i in frq]
        heapq.heapify(lst)
        return [heapq.heappop(lst)[1] for _ in range(k)]
            