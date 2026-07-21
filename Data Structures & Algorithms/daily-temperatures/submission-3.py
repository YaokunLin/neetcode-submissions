class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        result = [0] * len(temperatures)
        past_temps_unmatched = []

        for cur_day, cur_temp in enumerate(temperatures):
            while past_temps_unmatched and cur_temp > past_temps_unmatched[-1][-1]:
                # matching a temp
                last_day_unmatched, last_temp_unmatched = past_temps_unmatched.pop()
                result[last_day_unmatched] = (cur_day - last_day_unmatched)
            
            past_temps_unmatched.append((cur_day, cur_temp))

        return result

            
            


        
   
      
               

  
        