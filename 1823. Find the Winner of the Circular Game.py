class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def fwinner(i,j):
            if i==1:
                return 1
            return (fwinner(i-1,j)+j-1)%i+1
        val=fwinner(n,k)
        return val
            