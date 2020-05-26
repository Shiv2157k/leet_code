from typing import List


class RemoveElements:

    def remove_elements(self, nums: List[int], val: int) -> int:
        """
        Approach: Two pointers
        :param nums:
        :param val:
        :return:
        """
        if len(nums) == 0:
            return 0

        _len = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[_len] = nums[i]
                _len += 1
        return _len

    def remove_elements_(self, nums: List[int], val: int) -> int:
        """
        Approach: Two pointers from rare
        :param nums:
        :param val:
        :return:
        """
        if len(nums) == 0:
            return 0
        i, _len = 0, len(nums)
        while i < _len:
            if nums[i] == val:
                nums[i] = nums[_len - 1]
                _len -= 1
            else:
                i += 1
        return _len


if __name__ == "__main__":
    ele = RemoveElements()
    print(ele.remove_elements([3, 2, 2, 3, 4, 5, 6, 6], 3))
    print(ele.remove_elements_([3, 2, 2, 3, 4, 5, 6, 6], 3))
