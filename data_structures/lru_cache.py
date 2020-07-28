from collections import OrderedDict


class LRUCache_(OrderedDict):
    """
    Approach: Ordered Dictionary (HashMap + LinkedList)
    Time Complexity: O(1) for put and get
    Space Complexity: O(capacity)
    """
    def __init__(self, capacity):
        """
        :param capacity:
        """
        self.capacity = capacity

    def get(self, key):
        """
        Gets the key if exists else -1
        :param key:
        :return:
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        Creates or updates they key value pair.
        :param key:
        :param value:
        :return:
        """
        if key in self:
            self.move_to_end(key)
        # update the value
        self[key] = value
        if len(self) > len(self.capacity):
            self.popitem(last=False)


class DLinkedList:
    """
    Doubly Linked List Implementation.
    """
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    """
    Approach: Using Doubly Linked List
    Time Complexity: O(1)
    Space Complexity: O(capacity)
    """
    def _add_node(self, node):
        """
        Adds the node right after the head.
        :param node:
        :return:
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove existing node from linked list.
        :param node:
        :return:
        """
        prev = node.prev  # backwards
        new = node.next   # None

        prev.next = new  # None
        new.prev = prev  # prev value

    def _move_to_head(self, node):
        """
        Move certain node in between to head.
        :param node:
        :return:
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Gets the tail.
        :return:
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        Constructor for LRU Cache.
        :param capacity:
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedList(), DLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        Gets the value else -1.
        :param key:
        :return:
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        # move the accessed node to head
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        Creates or updates the node and its value.
        :param key:
        :param value:
        :return:
        """
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedList()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

