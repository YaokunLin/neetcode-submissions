class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -  1
        max_vol = 0
        while l < r:
            min_h = min(heights[l], heights[r])
            cur_vol = min_h * (r - l)
            max_vol = max(max_vol, cur_vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol
            

        