class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cur_vol = (r - l) * min(heights[r], heights[l])
            max_vol = max(cur_vol, max_vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol



       


 
              

     
            

        