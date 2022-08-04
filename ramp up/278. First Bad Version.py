# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        beg=0
        end=n
        while beg<=end:
            mid=(beg+end)//2
            if isBadVersion(mid):
                end = mid-1
            else:
                beg = mid+1
        return beg