import heapq
import random
from typing import List


class Array:

    def kth_largest_element_(self, nums: List[int], k: int) -> int:
        """
        Approach: Partition Algortihm
        Time Complexity: O(N) Worst Case: O(N^2)
        Space Complexity: O(1)
        :param nums:
        :param k:
        :return:
        """

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot = nums[pivot_index]
            # move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # move all smaller elements to left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left: int, right: int, k_smallest: int) -> int:
            # base case
            if left == right:
                return nums[left]
            # generate pivot index randomly
            pivot_index = random.randint(left, right)

            # find pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final position
            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif k_smallest < pivot_index:  # move left
                return select(left, pivot_index - 1, k_smallest)
            else:  # move right
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)

    def kth_largest_element(self, nums: List[int], k: int) -> int:
        """
        Approach: Heap
        Time Complexity: O(log N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappushpop(heap, nums[i])
        return heapq.heappop(heap)


if __name__ == "__main__":
    array = Array()
    print(array.kth_largest_element(
        [3, 2, 1, 5, 6, 4], 2
    ))
    
    print(array.kth_largest_element(
        [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    ))
    print(array.kth_largest_element_(
        [3, 2, 1, 5, 6, 4], 2
    ))
    print(array.kth_largest_element_(
        [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    ))
