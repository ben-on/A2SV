class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        mm,mx,n=points[0][0],points[0][1],len(points)
        res=0
        for i in range(1,n):
            if points[i][0] in range(mm,mx+1) or points[i][1] in range(mm,mx+1):
                mm=max(points[i][0],mm)
                mx=min(points[i][1],mx)
            else:
                mm,mx=points[i][0],points[i][1]
                res+=1
        res+=1
        return res