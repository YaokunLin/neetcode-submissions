class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        res_row = -1
        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif  matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                res_row = mid_row
                break
        if res_row == -1:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == matrix[res_row][mid]:
                return True
            elif target > matrix[res_row][mid]:
                l = mid + 1
            elif target < matrix[res_row][mid]:
                r = mid - 1
        return False

        


      
            

        