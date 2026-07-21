class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.count += 1
            self.cache[key][0] = self.count
            return self.cache[key][1]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        self.count += 1
        if key in self.cache:
            self.cache[key] = [self.count, value]
        else:
            if len(self.cache) >= self.capacity:
                least_key = min(self.cache, key=lambda k:self.cache[k][0])
                del self.cache[least_key]
                self.cache[key] = [self.count, value]
            else:
                self.cache[key] = [self.count, value]

            
    
            

        
