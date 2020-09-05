from typing import List

from heapq import *


class DataStream:
    """
    Approach: Using Heap Data Structure
    Time Complexity: O(log N) for adding and O(1) for finding.
    Space Complexity: O(1)
    """

    def __init__(self):
        # small to store small numbers n/2
        # large to store large numbers n/2 + 1
        self.small = []
        self.large = []

    def add_number(self, num):
        # if we add and length of small and large is same
        # then push it to large based on the comparing the
        # last small value
        # Scenarios:
        # Before adding:
        # 1. length of small and large is k, k
        # 2. length of small and large is k, k + 1
        # After adding:
        # 1. length of small and large is k, k + 1
        # 2. length of small and large is k + 1, k + 1
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def find_median(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]


if __name__ == "__main__":
    data_stream = DataStream()
    data_stream.add_number(3)
    data_stream.add_number(4)
    data_stream.add_number(1)
    data_stream.add_number(7)
    data_stream.add_number(9)
    data_stream.add_number(8)
    print(data_stream.small)
    print(data_stream.large)
    print(data_stream.find_median())