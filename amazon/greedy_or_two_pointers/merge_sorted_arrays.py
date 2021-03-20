from typing import List


class Array:

    def merge_sorted(self, nums1: List[int], m: int, nums2: List[int], n:int) -> List[int]:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1


if __name__ == "__main__":
    array = Array()
    print(array.merge_sorted(
        nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3
    ))