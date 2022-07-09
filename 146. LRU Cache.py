class LRUCache(OrderedDict):
    
    def __init__(self, capacity: int):
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, False)
            return self[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if self.capacity== len(self) and key not in self:
            self.popitem(last=True)
        self[key]=value
        self.move_to_end(key, False) 
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)