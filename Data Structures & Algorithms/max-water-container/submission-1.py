class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                curr_area = min(heights[j], heights[i]) * (j - i)
                max_area = max(max_area, curr_area)
        return max_area
              

     
            

        