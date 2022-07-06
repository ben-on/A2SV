class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        que,tot,idx = [],0,0
        while ladders>=0 and idx < len(heights)-1:
            temp = heights[idx] - heights[idx+1]
            if temp < 0:
                tot += abs(temp)
                bisect.insort(que, abs(temp))
                
                if tot > bricks and ladders == 0:
                    return idx
                
                elif tot > bricks:
                    tot -= que.pop()
                    ladders -= 1
            idx += 1
        return len(heights)-1
        