class StockSpanner:

    def __init__(self):
        self.stock_span = []

    def next(self, price: int) -> int:
        count = 1
      
        stock = self.stock_span.copy()
        while len(stock) > 0:
            if price >= stock[-1]:
                stock.pop()
                count += 1
            else:
                break
        self.stock_span.append(price)
        return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)