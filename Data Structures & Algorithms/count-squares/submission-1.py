class CountSquares:

    def __init__(self):
        self.square = {}
        
    def add(self, point: List[int]) -> None:
        key = tuple(point)
        if key in self.square:
            self.square[key] += 1
        else:
            self.square[key] = 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (px, py), count in self.square.items():
            #check diagonal
            if abs(px - py) != abs(x - y) or px == x or y == py:
                continue
            res += count * self.square.get((px, y), 0) * self.square.get((x, py), 0)
        return res
            
   

        
