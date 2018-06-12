class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            self.dict[key] = value
            if len(self.dict) > self.capacity:
                self.dict.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)