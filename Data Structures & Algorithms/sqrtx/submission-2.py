class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = -1
        while l <= r:
            mid = (r - l) // 2 + l
            if mid * mid > x:
                r = mid - 1
            elif mid * mid == x:
                return mid
            else:
                l = mid + 1
                res = mid

        return res
        
        