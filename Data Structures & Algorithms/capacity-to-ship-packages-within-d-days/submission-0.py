class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        def canShip(weights, max_carry):
            res = 1
            carry_w = 0
            for w in weights:
                if w + carry_w > max_carry:
                    res += 1
                    carry_w = w
                else:
                    carry_w += w
            return res

        while l <= r:
            mid = (r - l) // 2 + l
            if canShip(weights, mid) > days:
                l = mid + 1
            else:
                r = mid - 1
        return l

        