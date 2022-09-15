class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(matrix[i][j])
                if i>0 and matrix[i][j] ==1 and matrix[i-1][j]!= 0:
                    matrix[i][j] =  1 +  matrix[i-1][j] 
        # print(matrix)
        result = 0
        for rw in matrix:
            stack=[]
            for i,h in enumerate(rw):
                begin=i
                while stack and stack[-1][1]>h:
                    idx,ht=stack.pop()
                    result=max(result,ht*(i-idx))
                    begin=idx
                stack.append((begin,h))
            for i,h in stack:
                result=max(result,h*(len(rw)-i))
        return result
