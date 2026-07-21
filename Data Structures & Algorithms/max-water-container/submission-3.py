class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                cur_vol = (j - i) * min(heights[i], heights[j])
                res = max(res, cur_vol)
        return res


 
              

     
            

        