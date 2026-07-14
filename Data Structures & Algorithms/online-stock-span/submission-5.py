class StockSpanner:

    def __init__(self):
        self.stock = []



    def next(self, price: int) -> int:
        count  = 1
        i = len(self.stock) - 1
        while i >= 0 and self.stock[i] <= price:
            i -= 1
            count += 1
        self.stock.append(price)
        return count
      
       
      
    

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)