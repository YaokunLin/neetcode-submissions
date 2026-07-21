class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for i in range(self.rows):
            prefix = 0
            for j in range(self.cols):
                prefix += matrix[i][j]
                above = self.prefix_sum[i][j + 1]
                self.prefix_sum[i + 1][j + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2 + 1][col2 + 1]
        above = self.prefix_sum[row1][col2 + 1]
        left = self.prefix_sum[row2 + 1][col1]
        overlap = self.prefix_sum[row1][col1]
        res = total - above - left + overlap
        return res

     


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)