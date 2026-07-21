

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        sorted_pair = sorted(pair, reverse=True)
        stack = []
        for p, s in sorted_pair:
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            


       

       

        