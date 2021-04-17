from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, val: int):
        self[key] = val
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last=False)

class DLinkedNode:

    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LeastFrequentlyUsedCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: "DLinkedNode"):

        # node to head
        node.prev = self.head
        node.next = self.head.next

        # head to node
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: "DLinkedNode"):

        back = node.prev
        front = node.next

        back.next = front
        front.prev = back

    def _move_to_head(self, node: "DLinkedNode"):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> "DLinkedNode":
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, val: int):
        node = self.cache.get(key, None)
        if not node:
            new_node = DLinkedNode(key, val)
            self._add_node(new_node)
            self.cache[key] = new_node
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = val
            self._move_to_head(node)


if __name__ == "__main__":

    lru_cache = LRUCache(2)
    lru_cache_1 = LeastFrequentlyUsedCache(2)

    lru_cache.put(1, 1)
    lru_cache_1.put(1, 1)

    lru_cache_1.put(2, 2)
    lru_cache.put(2, 2)

    print(lru_cache.get(1))
    print(lru_cache_1.get(1))

    lru_cache.put(3, 3)
    lru_cache_1.put(3, 3)

    print(lru_cache.get(2))
    print(lru_cache_1.get(2))