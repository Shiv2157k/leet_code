from typing import List
from collections import deque


class SlidingWindow:

    def get_max_in_window__(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Brute Force
        Time Complexity: O(NK)
        Space Complexity: O(N - k + 1)
        :param nums:
        :return:
        """
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i: i + k]) for i in range(n - k + 1)]

    def get_max_in_window_(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Using Deque
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        size = len(nums)
        if size * k == 0:
            return []
        if size == 1:
            return nums

        queue, output, max_idx = deque(), [], 0

        def clean_up(index: int):
            # if there is an index not in the current
            # sliding window pop that out
            if queue and queue[0] == index - k:
                queue.popleft()
            # pop all the indexes that has values less than
            # current index value
            while queue and nums[index] > nums[queue[-1]]:
                queue.pop()

        # initiate deque
        for idx in range(k):
            clean_up(idx)
            queue.append(idx)
            if nums[idx] > nums[max_idx]:
                max_idx = idx
        output.append(nums[max_idx])

        # start adding all the max numbers from
        # a sliding window starting from kth index
        for idx in range(k, size):
            clean_up(idx)
            queue.append(idx)
            output.append(nums[queue[0]])
        return output

    def get_max_in_window(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        size = len(nums)
        if size * k == 0:
            return []
        if k == 1:
            return nums

        left, right = [0] * size, [0] * size
        left[0], right[size - 1] = nums[0], nums[size -  1]

        for l_idx in range(1, size):

            if l_idx % k == 0:
                left[l_idx] = nums[l_idx]
            else:
                left[l_idx] = max(left[l_idx - 1], nums[l_idx])

            r_idx = size - l_idx - 1
            if (r_idx + 1) % k == 0:
                right[r_idx] = nums[r_idx]
            else:
                right[r_idx] = max(right[r_idx + 1], nums[r_idx])

        output = []
        for idx in range(size - k + 1):
            output.append(max(left[idx + k - 1], right[idx]))

        return output


if __name__ == "__main__":
    window = SlidingWindow()
    print(window.get_max_in_window__([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(window.get_max_in_window_([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(window.get_max_in_window([1, 3, -1, -3, 5, 3, 6, 7], 3))