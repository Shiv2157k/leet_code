from typing import List
from collections import deque


class SlidingWindow:

    def get_all_max_(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        # edge cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        # initialize left and right array
        left, right = [0] * n, [0] * n
        left[0], right[n - 1] = nums[0], nums[n - 1]

        for lft_idx in range(1, n):
            # left -> right
            if lft_idx % k == 0:
                # block starts
                left[lft_idx] = nums[lft_idx]
            else:
                # add the max
                left[lft_idx] = max(left[lft_idx - 1], nums[lft_idx])
            # generate the current right
            right_idx = n - lft_idx - 1
            # right -> left
            if (right_idx + 1) % k == 0:
                # block starts
                right[right_idx] = nums[right_idx]
            else:
                # add the max
                right[right_idx] = max(right[right_idx + 1], nums[right_idx])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output

    def get_all_max(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Deque / Doubly Linked List
        Time Complexity: O(N) - since each elements is processed exactly twice.
        Space Complexity: O(N)
        - O (N - k + 1) is used for an o/p.
        - O(k) for a deque.
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        # edge case
        if n * k == 0:
            return []
        # if window size is 1 return the array
        if k == 1:
            return nums
        # initialize a deque i.e., doubly linked list
        # use it to store the indexes
        q = deque()

        # function that pops out and cleans the queue
        def clean_deque(index: int) -> None:
            # remove the queue if it is outside of the window
            if q and q[0] == index - k:
                q.popleft()
            # pop all the elements that are less than current
            # index value
            while q and nums[q[-1]] < nums[index]:
                q.pop()

        # initialize the deque with maximum window value
        max_index = 0
        result = []
        for index in range(k):
            # clean the queue
            clean_deque(index)
            # append the current index
            q.append(index)
            if nums[index] > nums[max_index]:
                max_index = index

        result = [nums[max_index]]

        for index in range(k, n):
            # clean the queue
            clean_deque(index)
            # append the current index
            q.append(index)
            # append the first left index value
            # to the result
            result.append(nums[q[0]])
        return result


if __name__ == "__main__":
    sliding_window = SlidingWindow()
    print(sliding_window.get_all_max(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ))
    print(sliding_window.get_all_max_(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ))



