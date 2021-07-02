class ListNode:

    def __init__(self, key: int=-1, val:int=-1, next=None):
        self.key = key
        self.val = val
        self.next =next


class HashMap:

    def __init__(self):
        self.key_space = 9973
        self.bucket = [None] * self.key_space

    def _hash(self, key: int):
        return key % self.key_space

    def get(self, key: int) -> int:

        hash_key = self._hash(key)
        if not self.bucket[hash_key]:
            return -1

        current = self.bucket[hash_key]

        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def put(self, key: int, value: int):

        hash_key = self._hash(key)
        if not self.bucket[hash_key]:
            self.bucket[hash_key] = ListNode(key, value)
            return
        current = self.bucket[hash_key]

        while current:
            if current.key == key:
                current.val = value
                return
            elif not current.next:
                break
            else:
                current = current.next
        current.next = ListNode(key, value)

    def remove(self, key: int):
        hash_key = self._hash(key)
        if not self.bucket[hash_key]:
            return
        current = self.bucket[hash_key]
        dummy = ListNode()
        dummy.next = current

        curr = dummy

        while curr and curr.next:

            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next
        self.bucket[hash_key] = dummy.next



