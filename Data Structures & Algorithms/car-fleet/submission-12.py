

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = {}
        for i in range(len(position)):
            position_speed_map[position[i]] = speed[i]
        sorted_position_speed = dict(sorted(position_speed_map.items(), key=lambda item:item[0]))
        stack = {}
        for key, val in sorted_position_speed.items():
            time_to_target = (target - key) / val
            stack[key] = time_to_target
        res = []
        for val in stack.values():
            if val not in res:
                while res and val > res[-1]:
                    res.pop()
                res.append(val)
        print(res)
        print(stack)
    
                
        return len(res)

            

        
      
      
     
            


       

       

        