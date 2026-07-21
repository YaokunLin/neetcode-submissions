class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    res.append((i, j))
        
        for r, c in res:
            for k in range(rows):
                matrix[k][c] = 0
            for j in range(cols):
                matrix[r][j] = 0

            

        
        