from collections import OrderedDict


class LRUCache_(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(Capacity)

        :param key:
        :return:
        """
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int):
        """
        Time Complexity: O(1)
        Space Complexity: O(Capacity)
        :param key:
        :param value:
        :return:
        """
        self[key] = value
        self.move_to_end(key)
        if self.capacity < len(self):
            self.popitem(last=False)


class DLinkedNode:

    def __init__(self, key: int = 0, val: int = 0, prev: int=None, next: int=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def __add_node(self, node: DLinkedNode):

        # node -> head
        node.prev = self.head
        node.next = self.head.next

        # head -> node
        self.head.next.prev = node
        self.head.next = node

    def __remove_node(self, node: DLinkedNode):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def __move_to_head(self, node: DLinkedNode):
        self.__remove_node(node)
        self.__add_node(node)

    def __pop_tail(self) -> DLinkedNode:
        prev_tail = self.tail.prev
        self.__remove_node(prev_tail)
        return prev_tail

    def get(self, key: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(Capacity)
        :param key:
        :return:
        """
        if key in self.cache:
            node = self.cache[key]
            self.__move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int):
        """
        Time Complexity: O(1)
        Space Complexity: O(Capacity)
        :param key:
        :param value:
        :return:
        """

        if key not in self.cache:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self.__add_node(new_node)
            self.size += 1

            if self.capacity < self.size:
                tail = self.__pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.cache[key] = node
            self.__move_to_head(node)


if __name__ == "__main__":

    lru_cache = LRUCache(2)
    lru_cache.put(9, 11)
    lru_cache.put(10, 11)
    print(lru_cache.get(9))
    lru_cache.put(13, 19)
    print(lru_cache.get(10))
