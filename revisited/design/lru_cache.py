class DHashLinkedNode:
    """
    Hash Map Doubly Linked List
    """
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache Design
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        self.head, self.tail = DHashLinkedNode(), DHashLinkedNode()

        # build the bi-direction b/w head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """
        Add right after the head.
        :param node:
        :return:
        """
        # node -> head
        node.prev = self.head
        node.next = self.head.next

        # head -> node
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove the given node.
        :param node:
        :return:
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move the node to head.
        :param node:
        :return:
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pops the current tail.
        :return:
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    # get key
    def get(self, key):
        """
        Gets the value if a key exists else returns -1
        :param key:
        :return:
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    # put key value
    def put(self, key, value):
        """
        Puts if there exists else creates one.
        :param key:
        :param value:
        :return:
        """
        node = self.cache.get(key)
        # create a new_node
        if not node:

            new_node = DHashLinkedNode()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:  # update the value
            node.value = value
            self._move_to_head(node)


if __name__ == "__main__":
    lru = LRUCache(5)
    lru.put(19, 7)
    lru.put(20, 5)
    lru.put(23, 5)
    lru.put(7, 9)
    lru.put(10, 7)
    print(lru.get(19))
    print(lru.get(7))
    print(lru.get(13))
    lru.put(6, 7)
    print(lru.get(6))