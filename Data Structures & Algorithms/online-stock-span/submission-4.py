class StockSpanner:

    def __init__(self):
        self.stock_span = []

    def next(self, price: int) -> int:
        count = 1
        i = len(self.stock_span) - 1
        while i >= 0 and price >= self.stock_span[i]:
            i -= 1
            count += 1
        self.stock_span.append(price)
        return count
      
    

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)