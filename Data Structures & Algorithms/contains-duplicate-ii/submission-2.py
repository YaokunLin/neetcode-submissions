class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = i
            else:
                exist_index = nums_map[nums[i]]
                if abs(i - exist_index) <= k:
                    return True
                else:
                    nums_map[nums[i]] = i
        print(nums_map)
        return False

        