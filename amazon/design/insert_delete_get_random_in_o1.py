from random import choice


class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        # insert key: val, val: index into hash map.
        if val not in self.map:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            # move the last element to current index
            last_element, idx = self.list[-1], self.map[val]
            self.map[last_element], self.list[idx] = idx, last_element
            self.list.pop()
            del self.map[val]
            return True
        return False

    def get_random(self) -> int:
        return choice(self.list)


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.insert(9))
    print(obj.insert(9))
    print(obj.insert(5))
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.get_random())