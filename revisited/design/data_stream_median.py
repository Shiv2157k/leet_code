from heapq import *


class DataStream:
    """
    Using Priority Queue
    heapq data structure
    """

    def __init__(self):
        self.small = []
        self.large = []

    def add_number(self, num: int):
        # if the small max heap and large min heap lengths
        # are same then add it to the large min heap.
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # if the lengths are not equal push it into the
            # small heap and make it negative for the order
            # to get the median from the top
            heappush(self.small, -heappushpop(self.large, num))

    def find_median(self):
        # if it is even
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else: # odd
            return self.large[0]


if __name__ == "__main__":
    data_stream = DataStream()
    data_stream.add_number(2)
    data_stream.add_number(1)
    print(data_stream.find_median())
    data_stream.add_number(3)
    print(data_stream.find_median())
    data_stream.add_number(4)
    print(data_stream.find_median())
