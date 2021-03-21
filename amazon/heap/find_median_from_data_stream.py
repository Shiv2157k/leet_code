import heapq


class DataStream:
    """
    Approach: Heap
    Time Complexity: O(log N)
    Space Complexity: O(N)
    """

    def __init__(self):
        self.large = []
        self.small = []

    def add_num(self, num: int) -> None:

        if len(self.small) == len(self.large):
            # prioritize to the max heap
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            # prioritize to min heap
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self) -> float:
        if len(self.small) == len(self.large):  # even
            return float(self.large[0] - self.small[0]) / 2.0
        else:  # odd
            return float(self.large[0])


if __name__ == "__main__":
    data_stream = DataStream()
    data_stream.add_num(1)
    print(data_stream.find_median())
    data_stream.add_num(2)
    print(data_stream.find_median())
    data_stream.add_num(3)
    print(data_stream.find_median())
