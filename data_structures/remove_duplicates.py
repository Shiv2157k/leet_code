from typing import List


class RemoveDuplicates:

    def remove_duplicates(self, nums: List) -> int:

        if len(nums) == 0:
            return 0
        len_ = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_


if __name__ == "__main__":
    result = RemoveDuplicates()
    print(result.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))