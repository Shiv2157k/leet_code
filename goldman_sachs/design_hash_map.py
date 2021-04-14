class ListNode:

    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    """
    1. Need to implement hash function
        - map an i/p to fixed size O(1)
    2. Insertion
        - use hash function to find the block, insert on linked list O(1).
    3. Removal
        - use hash function to find block, removal on linked list O(1).
    4. Search:
        - use hash function to find the block, find an element in linked list O(1).
    """

    def __init__(self):

        self.key_space = 9973
        self.bucket = [None] * self.key_space

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def get(self, key: int) -> int:
        """
        Gets the value if exists.
        :param key:
        :return:
        """
        hash_key = self._hash(key)
        # edge case
        if not self.bucket[hash_key]:
            return -1
        current = self.bucket[hash_key]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        # if bucket is present but no key
        # present in that bucket.
        return -1

    def put(self, key: int, value: int):
        """
        If key already exists modified the value
        else creates a new list node.
        :param key:
        :param value:
        :return:
        """
        hash_key = self._hash(key)
        # edge case
        # if there is no bucket with that hash key
        # create one
        if not self.bucket[hash_key]:
            self.bucket[hash_key] = ListNode(key, value)
            return
        current = self.bucket[hash_key]
        while current:
            if current.key == key:
                current.val = value
                return
            if not current.next:
                break
            else:
                current = current.next
        current.next = ListNode(key, value)

    def remove(self, key: int):
        hash_key = self._hash(key)
        # edge case
        if not self.bucket[hash_key]:
            return
        head = self.bucket[hash_key]
        dummy = ListNode()
        dummy.next = head

        curr = dummy
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next
        self.bucket[hash_key] = dummy.next


if __name__ == "__main__":
    dictionary = MyHashMap()
    dictionary.put(1, 2)
    print(dictionary.get(1))
    dictionary.put(1, 9)
    print(dictionary.get(1))
    dictionary.remove(1)
    print(dictionary.get(1))
    dictionary.put(3, 5)
    dictionary.put(9, 100)
    print(dictionary.get(3))
    print(dictionary.get(9))
