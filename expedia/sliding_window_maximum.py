from typing import List
from collections import deque


class Window:

    def max_in_sliding(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Deque
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        q = deque()

        def clean_queue(index: int):
            if q and q[0] == index - k:
                q.popleft()
            while q and nums[q[-1]] < nums[index]:
                q.pop()

        max_index = 0

        for index in range(k):
            clean_queue(index)
            q.append(index)
            if nums[index] > nums[max_index]:
                max_index = index

        window_max = [nums[max_index]]

        for index in range(k, n):
            clean_queue(index)
            q.append(index)
            window_max.append(nums[q[0]])
        return window_max

    def max_while_sliding(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        left, right = [0] * n, [0] * n
        left[0], right[-1] = nums[0], right[-1]

        for l_idx in range(1, n):
            if l_idx % k == 0:  # new window
                left[l_idx] = nums[l_idx]
            else:
                left[l_idx] = max(left[l_idx - 1], nums[l_idx])

            r_idx = n - l_idx - 1
            if (r_idx + 1) % k == 0:
                right[r_idx] = nums[r_idx]
            else:
                right[r_idx] = max(right[r_idx + 1], nums[r_idx])
        window_max = []
        for idx in range(n - k + 1):
            window_max.append(max(left[idx + k - 1], right[idx]))
        return window_max


if __name__ == "__main__":
    window = Window()
    print(window.max_in_sliding([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(window.max_while_sliding([1, 3, -1, -3, 5, 3, 6, 7], 3))