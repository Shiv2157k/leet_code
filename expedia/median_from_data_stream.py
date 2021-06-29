from heapq import heappushpop, heappush


class DataStream:
    """
    Time Complexity: O(5 * log N) + O(1) == O(log N)
    3 insertions + 2 deletions.
    Space Complexity: O(N)
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_number(self, num: int):

        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def find_median(self):

        if len(self.min_heap) == len(self.max_heap):
            return float(self.max_heap[0] - self.min_heap[0]) / 2.0
        else:
            return float(self.max_heap[0])


if __name__ == "__main__":
    data_stream = DataStream()
    data_stream.add_number(1)
    print(data_stream.find_median())
    data_stream.add_number(3)
    print(data_stream.find_median())
    data_stream.add_number(5)
    print(data_stream.find_median())
    data_stream.add_number(2)
    print(data_stream.find_median())