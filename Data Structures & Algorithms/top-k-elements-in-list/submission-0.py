class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = {}
        for num in nums:
            if num not in visited: 
                visited[num] = 1
            else:
                visited[num] += 1
        sorted_visited = sorted(visited.items(), key=lambda x: x[1], reverse=True)
        res = [num[0] for num in sorted_visited[:k]]
        return res
       