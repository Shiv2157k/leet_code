class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key: int):
        for k, v in self.bucket:
            if key == k:
                return v
        return -1

    def update(self, key: int, value: int):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key: int):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class HashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # made it a prime number for less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(2069)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


if __name__ == "__main__":
    obj = HashMap()
    obj.put(4, 5)
    obj.put(9, 10)
    param_2 = obj.get(4)
    print(param_2)
    print(obj.get(9))
    obj.remove(4)