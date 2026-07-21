class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_sum(piles, speed)->int:
            total_sum = 0
            for val in piles:
                rounded_val = math.ceil(val / speed)
                total_sum += rounded_val
            return total_sum

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            curr_h = hours_sum(piles, mid)
            if curr_h > h:
                l = mid + 1
            elif curr_h <= h:
                r = mid - 1
                res = mid
        return res

        