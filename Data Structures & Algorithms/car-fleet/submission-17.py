

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = {}
        for i in range(len(position)):
            position_speed_map[position[i]] = speed[i]
        sorted_position_speed = dict(sorted(position_speed_map.items(), key=lambda item:item[0], reverse=True))
        stack = []
        for key, val in sorted_position_speed.items():
            time_to_target = (target - key) / val
            stack.append(time_to_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


            

        
      
      
     
            


       

       

        