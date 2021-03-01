from collections import defaultdict, OrderedDict


class Node:

    def __init__(self, val: int, freq: int):
        self.val = val
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_nodes = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key: int):
        if key not in self.cache:
            return -1
        node = self.cache[key]

        # delete the current freq storage bucket
        del self.freq_nodes[node.freq][key]

        # since there is a get operation
        # increase its frequency by 1
        node.freq += 1
        # update it to the new freq storage
        self.freq_nodes[node.freq][key] = node

        # if there is no node present with min freq
        # update the min freq
        if not self.freq_nodes[self.min_freq]:
            self.min_freq += 1
        return node.val

    def put(self, key: int, val: int):
        # validation
        if not self.capacity:
            return
        # if it is already in cache
        if key in self.cache:
            self.cache[key].val = val
            self.get(key)
            return
        # if reached the capacity
        if len(self.cache) == self.capacity:
            # remove the least frequently used
            lfu_key, _ = self.freq_nodes[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]

        # create a new item
        new_node = Node(val, 1)
        self.cache[key] = new_node
        self.freq_nodes[new_node.freq][key] = new_node
        self.min_freq = 1


if __name__ == "__main__":
    lfu_cache = LFUCache(3)
    print(lfu_cache.get(3))
    lfu_cache.put(1, 19)
    print(lfu_cache.get(1))
    lfu_cache.put(3, 9)
    lfu_cache.put(2, 8)
    print(lfu_cache.get(1))
    lfu_cache.put(4, 7)
    print(lfu_cache.get(2))
    print(lfu_cache.get(3))
