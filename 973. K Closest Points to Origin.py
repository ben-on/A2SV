class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lis=[]
        newlis=[]
        for i in range(len(points)):
            lis.append(((points[i][0])**2)+((points[i][1])**2))
        lis.sort()
        maxx = lis[k-1]
        for i in range(len(points)):
            if ((points[i][0])**2)+((points[i][1])**2)<=maxx:
                newlis.append(points[i])
        return newlis
                