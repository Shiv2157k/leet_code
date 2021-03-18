from collections import OrderedDict


class LRUCache(OrderedDict):
    """
    Approach: Ordered Dictionary DS
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, val: int):
        if key in self:
            self.move_to_end(key)
        self[key] = val
        if self.capacity < len(self):
            self.popitem(last=False)


class DLinkedNode:

    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None


class LeastRecentlyUsedCache:

    """
    Approach: Hash Map + Doubly LinkedList
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def __init__(self, capacity):
        # to maintain size
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.cache = dict()

        # link the head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # method to add node right next to head
    def _add_node(self, node):

        # head to node
        node.prev = self.head
        node.next = self.head.next

        # node to head
        self.head.next.prev = node
        self.head.next = node

    # method to remove node
    def _remove_node(self, node):

        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    # method certain in b/w to the head/
    def _move_to_head(self, node):

        self._remove_node(node)
        self._add_node(node)

    # method to remove node when capacity exceeds
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key, val):

        node = self.cache.get(key)
        if node:
            node.val = val
            # move the node right next to head
            self._move_to_head(node)
        else:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.val = val

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1


if __name__ == "__main__":
    lru_1 = LRUCache(3)
    lru = LeastRecentlyUsedCache(3)
    print(lru_1.get(1))
    print(lru.get(1))
    lru.put(9, 99)
    lru_1.put(9, 99)
    lru.put(3, 33)
    lru_1.put(3, 33)
    print(lru.get(9))
    print(lru_1.get(9))
    lru.put(7, 77)
    lru_1.put(7, 77)
    lru.put(5, 55)
    lru_1.put(5, 55)
    print(lru.get(5))
    print(lru_1.get(5))
    print(lru.get(3))
    print(lru_1.get(3))

