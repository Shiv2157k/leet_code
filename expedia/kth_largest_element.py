from typing import List
from heapq import heappush, heappop, heappushpop


class Array:

    def find_kth_largest_element(self, nums: List[int], k: int):
        """
        Approach: Heap
        Time Complexity: O(N log K)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        heap = []

        for i in range(len(nums)):
            if len(heap) < k:
                heappush(heap, nums[i])
            else:
                heappushpop(heap, nums[i])
        return heappop(heap)


if __name__ == "__main__":
    array = Array()
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 2))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 1))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 3))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 4))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 5))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 6))
    print(array.find_kth_largest_element([2, 3, 4, 5, 7, 11, 9], 7))
