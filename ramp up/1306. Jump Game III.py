class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        qu=deque([start])
        vis=set()
        while qu:
            r=len(qu)
            for i in range(r):
                temp=qu.popleft()
                vis.add(temp)
                if arr[temp]==0:
                    return True
                if temp+arr[temp] in range(len(arr)) and temp+arr[temp] not in vis:
                    qu.append(temp+arr[temp])
                if temp-arr[temp] in range(len(arr)) and temp-arr[temp] not in vis:
                    qu.append(temp-arr[temp])
        return False