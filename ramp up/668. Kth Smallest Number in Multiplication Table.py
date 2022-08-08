class Solution:
    def findKthNumber(self, m, n, k):
        left, right = 1, m*n
        while left <= right:
            mid = (left + right)//2
            if sum([min(mid//i, n) for i in range(1, m+1)]) < k:
                left = mid + 1
            else:
                right = mid -1
        return left
    
    
        # #brute force
        # lst=[]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         lst.append(i*j)
        # lst.sort()
        # return lst[k-1]