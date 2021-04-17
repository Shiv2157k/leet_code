import heapq


class DataStream:

    def __init__(self):
        self.small = []
        self.large = []

    def add(self, num: int):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


if __name__ == "__main__":
    data_stream = DataStream()
    data_stream.add(1)
    data_stream.add(2)
    print(data_stream.find_median())
    data_stream.add(3)
    print(data_stream.find_median())