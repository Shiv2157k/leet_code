from typing import List


class Array:

    def find_median(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search
        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        left, right = 0, x

        while left <= right:

            pX = left + (right - left) // 2
            pY = (x + y + 1) // 2 - pX

            l1 = float("-inf") if pX == 0 else nums1[pX - 1]
            r1 = float("inf") if pX == x else nums1[pX]

            l2 = float("-inf") if pY == 0 else nums2[pY - 1]
            r2 = float("inf") if pY == y else nums2[pY]

            if l1 > r2:
                right = pX - 1
            elif l2 > r1:
                left = pX + 1
            else:
                if (x + y) % 2 == 1:  # odd
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0


if __name__ == "__main__":

    array = Array()
    print(array.find_median([1, 3], [2]))
    print(array.find_median([1, 2], [3, 4]))
