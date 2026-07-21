from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
         
    def get(self, key: str, timestamp: int) -> str:
        value_timestamp = self.time_map[key]
        if len(value_timestamp) == 0:
            return ""
        sorted_value_stamp = sorted(value_timestamp, key = lambda x: x[1])
        res = []
        for value, time in sorted_value_stamp:
            if time <= timestamp:
                res.append([value, time])
    
        if len(res) == 0:
            return ""
        sorted_res = sorted(res, key = lambda x: x[1])
        return sorted_res[-1][0]



        
