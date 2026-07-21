class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num
            remain = prefix_sum - k
            if remain in prefix_count:
                count += prefix_count[remain]
            
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count