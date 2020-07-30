from typing import List


class TwoSortedArray:

    def get_median(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        left = 0
        right = x

        while left <= right:

            partition_x = (left + right) // 2
            partition_y = ((x + y + 1) // 2) - partition_x

            max_left_num1 = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            min_right_num1 = float("inf") if partition_x == x else nums1[partition_x]

            max_left_num2 = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_num2 = float("inf") if partition_y == y else nums2[partition_y]

            if max_left_num1 <= min_right_num2 and max_left_num2 <= min_right_num1:
                if (x + y) % 2 == 1:
                    return max(max_left_num1, max_left_num2)
                else:
                    return (max(max_left_num1, max_left_num2) + min(min_right_num1, min_right_num2)) / 2.0
            elif max_left_num1 > min_right_num2:
                right = partition_x - 1
            else:
                left = partition_x + 1


if __name__ == "__main__":

    two_sorted_array = TwoSortedArray()
    print(two_sorted_array.get_median([1, 2], [6]))
    print(two_sorted_array.get_median([13, 14, 45], [8, 9, 10, 11]))
    print(two_sorted_array.get_median([13], [11]))
    print(two_sorted_array.get_median([19], []))
    print(two_sorted_array.get_median([], [11]))

