from typing import List
from collections import deque


class Array:

    def shortest_sub_array_with_sum_atleast_k(self, nums: List[int], K: int) -> int:
        """
        Approach: Sliding Window
        Time Complexity:
        Space Complexity: O(N)
        :param nums:
        :param K:
        :return:
        """

        sum_at_index = [0]
        for num in nums:
            sum_at_index.append(sum_at_index[-1] + num)

        q = deque()
        # to store min sub array size
        # below value is the worst case
        # which would never happen.
        min_size = len(nums) + 1

        for index, value in enumerate(sum_at_index):
            # condition to maintain increasing order
            # in the queue
            while q and value <= sum_at_index[q[-1]]:
                q.pop()
            # condition to check minimum sub array with at least k sum
            # add each sum index into queue
            while q and value - sum_at_index[q[0]] >= K:
                min_size = min(min_size, index - q.popleft())
            q.append(index)
        return min_size if min_size < len(nums) + 1 else -1


if __name__ == "__main__":
    array = Array()
    print(array.shortest_sub_array_with_sum_atleast_k([2, -1, 2], 3))
    print(array.shortest_sub_array_with_sum_atleast_k([1], 1))
    print(array.shortest_sub_array_with_sum_atleast_k([1, 2], 4))