

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = {}
        for i in range(len(position)):
            position_speed_map[position[i]] = speed[i]
        sorted_position_speed = dict(sorted(position_speed_map.items(), key=lambda item:item[0]))
        stack = []
        for key, val in sorted_position_speed.items():
            time_to_target = (target - key) / val
            if time_to_target not in stack:
                while stack and stack[-1] < time_to_target:
                    stack.pop()

                stack.append(time_to_target)
        return len(stack)


            

        
      
      
     
            


       

       

        