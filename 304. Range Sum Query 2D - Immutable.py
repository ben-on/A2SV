class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
    
        m = len(matrix)
        n = len(matrix[0])
        presum = self.presum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m +1):
            for j in range(n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        presum = self.presum
        return presum[row2+1][col2+1] - presum[row1][col2+1] - presum[row2+1][col1] + presum[row1][col1]
    
    


#     def __init__(self, matrix: List[List[int]]):
#         self.arr=matrix

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         s=0
#         for i in range(row1,row2+1):
#             for j in range(col1,col2+1):
#                 s+=self.arr[i][j]
#         return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)