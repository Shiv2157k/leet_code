from collections import defaultdict, OrderedDict


class Node:

    def __init__(self, value:int = None, freq: int =None):
        self.val = value
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_bucket = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        del self.freq_bucket[node.freq][key]

        node.freq += 1
        self.freq_bucket[node.freq][key] = node

        if not self.freq_bucket[self.min_freq]:
            self.min_freq += 1
        return node.val

    def put(self, key: int, value: int):

        if not self.capacity:
            return

        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return

        if len(self.cache) == self.capacity:
            lfu_key, _ = self.freq_bucket[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]

        new_node = Node(value, 1)
        self.cache[key] = new_node
        self.freq_bucket[1][key] = new_node
        self.min_freq = 1
