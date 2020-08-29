from typing import List
from collections import deque


class SlidingWindow:

    def get_max_from_window(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        # base case
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left, right = [0] * n, [0] * n
        left[0], right[n - 1] = nums[0], nums[n - 1]

        # generate left to right and right to left
        # to place in the left and right arrays
        for i in range(1, n):
            # left -> right
            # block starts
            if i % k == 0:
                left[i] = nums[i]
            # put the max of previous and current
            else:
                left[i] = max(left[i - 1], nums[i])

            # right to left
            j = n - i - 1

            # block starts
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output

    def get_max_from_window_(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Using DS Deque.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        # base case
        if n * k == 0:
            return []
        if k == 1:
            return nums

        # clean up the deque
        def clean_up_queue(index: int):

            # if you have reached the window
            if queue and queue[0] == index - k:
                queue.popleft()

            # remove all if the current is greater
            while queue and nums[index] > nums[queue[-1]]:
                queue.pop()

        # initiate the queue and output
        queue = deque()
        max_index = 0
        for index in range(k):
            clean_up_queue(index)
            queue.append(index)

            if nums[index] > nums[max_index]:
                max_index = index
        output = [nums[max_index]]

        # build the outputs
        for index in range(k, n):
            clean_up_queue(index)
            queue.append(index)
            output.append(nums[queue[0]])
        return output


if __name__ == "__main__":
    sliding_window = SlidingWindow()
    print(sliding_window.get_max_from_window_([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sliding_window.get_max_from_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

