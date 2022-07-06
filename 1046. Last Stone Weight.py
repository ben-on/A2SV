class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            l=len(stones)    
            y=-heapq.heappop(stones)
            x=-heapq.heappop(stones)
            
            if y!=x:
                heapq.heappush(stones,-(y-x))
            elif l==2:
                heapq.heappush(stones,-(y-x))
        return -stones[0]
                