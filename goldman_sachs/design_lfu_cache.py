from collections import defaultdict, OrderedDict


class Node:

    def __init__(self, value:int = None, freq: int =None):
        self.val = value
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_bucket = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        del self.freq_bucket[node.freq][key]

        node.freq += 1
        self.freq_bucket[node.freq][key] = node

        if not self.freq_bucket[self.min_freq]:
            self.min_freq += 1
        return node.val

    def put(self, key: int, value: int):

        if not self.capacity:
            return

        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return

        if len(self.cache) == self.capacity:
            lfu_key, _ = self.freq_bucket[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]

        new_node = Node(value, 1)
        self.cache[key] = new_node
        self.freq_bucket[1][key] = new_node
        self.min_freq = 1

    def fractionAddition(self, expression: str) -> str:

        if not expression:
            return "0/1"

        if expression[0] != "-":
            expression = "+" + expression

        # parsing expression to numerator and denominators

        numerator, denominator = [], []
        index = 0

        while index < len(expression):

            is_positive = True if expression[index] == "+" else False

            # get numerator
            index += 1
            n = 0
            while expression[index].isdigit():
                n = n * 10 + int(expression[index])
                index += 1
            numerator.append(n if is_positive else -n)

            # get denominator
            index += 1
            d = 0
            while index < len(expression) and expression[index].isdigit():
                d = d * 10 + int(expression[index])
                index += 1
            denominator.append(d)

        common_divisor = 1
        for integer in denominator:
            common_divisor *= integer

        for i, (n, d) in enumerate(zip(numerator, denominator)):
            numerator[i] = n * common_divisor // d

        numerator_sum = 0
        for n in numerator:
            numerator_sum += n

        gcd = self.gcd(numerator_sum, common_divisor)

        numerator = numerator_sum // gcd
        denominator = common_divisor // gcd

        return f"{numerator}/{denominator}"
