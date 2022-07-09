class Solution:
    def goodDaysToRobBank(self, A, t):
        n = len(A)
        def incGaurd(A):
            arr = [0] * n
            for i in range(1,n):
                if A[i-1] >= A[i]:
                    arr[i] = arr[i-1] + 1
            return arr
        _inc,_dec = incGaurd(A),incGaurd(A[::-1])[::-1]
        ans = []
        for i in range(n):
            if _inc[i] >= t and _dec[i] >= t:
                ans.append(i)
        return ans