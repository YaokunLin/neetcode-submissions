from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        freq_sum = defaultdict(int)
        freq_sum[0] = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            remain = cur_sum - k
            count += freq_sum[remain]
            freq_sum[cur_sum] += 1
        return count 

     