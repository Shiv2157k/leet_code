from typing import List


class Array:

    def find_median(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search
        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        :param nums1:
        :param nums2:
        :return:
        """

        # swap the nums1 and nums2
        # we would always want nums1 to be smaller one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        left, right = 0, x

        while left <= right:

            # pivot for num1 array
            pX = left + (right - left) // 2
            # pivot for num2 array
            pY = (x + y + 1) // 2 - pX

            # initialize the left maximums and right minimums of two arrays
            left_max_x = float("-inf") if pX == 0 else nums1[pX - 1]
            right_min_x = float("inf") if pX == x else nums1[pX]
            left_max_y = float("-inf") if pY == 0 else nums2[pY - 1]
            right_min_y = float("inf") if pY == y else nums2[pY]

            if left_max_x > right_min_y:
                right = pX - 1
            elif left_max_y > right_min_x:
                left = pX + 1
            else:  # left_max_x < right_min_y and left_max_y < right_min_x
                # calculate the median and return
                if (x + y) % 2 == 1:  # odd
                    return max(left_max_x, left_max_y)
                else:  # even
                    return (max(left_max_x, left_max_y) + min(right_min_x, right_min_y)) / 2.0


if __name__ == "__main__":
    array = Array()
    print(array.find_median(
        [2, 3, 6, 7], [1, 5, 8, 10, 18, 20]
    ))
    print(array.find_median(
        [2, 3, 6, 7], [1, 8, 10, 18, 20]
    ))