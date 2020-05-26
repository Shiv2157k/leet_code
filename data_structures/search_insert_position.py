from typing import List


class SearchInsertPosition:

    def search_insert_positon(self, nums: List[int], target: int):

        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] < target:
                left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                return pivot
        return left


if __name__ == "__main__":
    srp = SearchInsertPosition()
    print(srp.search_insert_positon([1, 3, 4, 8, 9], 6))
    print(srp.search_insert_positon([1, 2, 3, 4], 4))
    print(srp.search_insert_positon([0, 1, 2, 3, 4], 1))
    print(srp.search_insert_positon([1, 2, 3, 4], 0))
