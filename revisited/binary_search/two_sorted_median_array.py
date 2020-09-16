from typing import List


class TwoSortedList:

    def get_median(self, nums_1: List[int], nums_2: List[int]) -> float:
        """
        Approach: Binary Search
        Time Complexity: O(log(min(x, y)))
        Space Complexity: O(1)
        :param nums_1:
        :param nums_2:
        :return:
        """

        # if nums_1 is greater than nums_2
        # swap the nums_1 and nums_2
        # nums_1 should be always considered as smaller length.
        if len(nums_1) > len(nums_2):
            nums_1, nums_2 = nums_2, nums_1

        # x - length of nums_1, which is always smaller than nums_2
        # y - length of nums_2
        x, y = len(nums_1), len(nums_2)

        # left - starts with 0
        # right - starts with length of x
        left, right = 0, x

        # perform binary search
        while left <= right:

            # pX - pivot of nums_1
            pX = (left + right) // 2
            # pY - pivot of nums_2
            pY = (x + y + 1) // 2 - pX

            # maximum number from left half of the nums1
            left_max_x = float("-inf") if pX == 0 else nums_1[pX - 1]
            # minimum number from right half of the nums1
            right_min_x = float("inf") if pX == x else nums_1[pX]

            # maximum number from left half of the nums2
            left_max_y = float("-inf") if pY == 0 else nums_2[pY - 1]
            # minimum number from right half of the nums2
            right_min_y = float("inf") if pY == y else nums_2[pY]

            # if the left max of x is less than or equals to right min of y
            # and right max of y is less than or equal to right min of x
            # we consider this as a valid 4 element formation to determine
            # the median.
            if left_max_x <= right_min_y and left_max_y <= right_min_x:
                # to determine odd combination
                if (x + y) % 2 == 1:
                    return max(left_max_x, left_max_y)
                else:
                    return (max(left_max_x, left_max_y) + min(right_min_x, right_min_y)) / 2.0
            # else if the left_max_x is greater than the right min y
            # need to move pivot to left
            elif left_max_x > right_min_y:
                right = pX - 1
            else:  # need to move the pivot towards right
                left = pX + 1


if __name__ == "__main__":
    sorted_list = TwoSortedList()
    print(sorted_list.get_median([3, 7, 9, 15, 18, 21, 25], [4, 6, 8, 10, 11, 18]))
    print(sorted_list.get_median([1, 3], [2]))
    print(sorted_list.get_median([1, 2], [3, 4]))
    print(sorted_list.get_median([0, 0], [0, 0]))


