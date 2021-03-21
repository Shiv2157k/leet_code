from collections import defaultdict, OrderedDict


class Node:

    def __init__(self, value: int, count: int):
        self.value = value
        self.freq = count


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.frequency_bucket = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]

        # del current freq storage bucket
        del self.frequency_bucket[node.freq][key]

        # increase the freq count
        node.freq += 1

        # update it to new frequency bucket
        self.frequency_bucket[node.freq][key] = node
        # update the frequency count
        if not self.frequency_bucket[self.min_freq]:
            self.min_freq += 1
        return node.value

    def put(self, key, value):
        # base case
        if not self.capacity:
            return
        # if already exists
        if key in self.cache:
            self.cache[key].value = value
            # for moving it to latest freq bucket
            # incrementing freq count
            self.get(key)
            return
        # if the capacity exceeds
        if len(self.cache) == self.capacity:
            lfu_key, _ = self.frequency_bucket[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]

        # if it is a new one create it
        new_node = Node(value, 1)
        self.cache[key] = new_node
        self.frequency_bucket[1][key] = new_node
        self.min_freq = 1


if __name__ == "__main__":
    lfu_cache = LFUCache(5)
    print(lfu_cache.get(3))
    lfu_cache.put(1, 19)
    print(lfu_cache.get(1))
    lfu_cache.put(3, 9)
    lfu_cache.put(2, 8)
    print(lfu_cache.get(1))
    lfu_cache.put(4, 7)
    print(lfu_cache.get(2))
    print(lfu_cache.get(3))
