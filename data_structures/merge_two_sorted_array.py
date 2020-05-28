from typing import List


class MergeTwoSortedArray:

    def get_merged_array(self, arr1: List[int], m: int, arr2: List[int], n: int) -> List[int]:
        """
        Two Pointers from right side of the list.
        :param arr1:
        :param m:
        :param arr2:
        :param n:
        :return:
        """

        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if arr1[p1] < arr2[p2]:
                arr1[p] = arr2[p2]
                p2 -= 1
            else:
                arr1[p] = arr1[p1]
                p1 -= 1
            p -= 1
        arr1[:p2 + 1] = arr2[:p2 + 1]
        return arr1


if __name__ == "__main__":
    merge = MergeTwoSortedArray()
    print(merge.get_merged_array([1, 2, 3, 4, 6, 0, 0, 0], 5, [2, 5, 6], 3))