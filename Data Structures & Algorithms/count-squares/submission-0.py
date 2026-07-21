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
            # (px, py) and (x, y) should be diagonal
            if abs(px - py) != abs(x - y) or x == px or y == py:
                continue
            res += self.square[(px, py)] * self.square.get((x, py), 0) * self.square.get((px, y), 0)
        return res

        
