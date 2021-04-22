from typing import List


class Array:

    def is_circular(self, nums: List[int]) -> bool:
        """
        Approach: Fast and Slow Pointer
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        for i in range(len(nums)):

            if nums[i] == 0:
                continue

            direction = (nums[i] > 0)

            slow = fast = i

            # 1. check for cycle
            while nums[slow] != 0 or nums[fast] != 0:
                slow = self.__next(nums, slow, direction)
                fast = self.__next(nums, self.__next(nums, fast, direction), direction)

                if slow == -1 or fast == -1:
                    break
                elif slow == fast:
                    return True

            # mark all the visited nodes
            slow = i
            while self.__next(nums, slow, direction) != -1:
                nums[slow] = 0
        return False

    def __next(self, nums, index, direction) -> int:
        """

        :param nums:
        :param index:
        :param direction:
        :return:
        """
        if index == -1:
            return -1
        elif (nums[index] > 0) != direction:
            return -1
        next_idx = (index + nums[index]) % len(nums)
        if next_idx < 0:
            next_idx += len(nums)
        return -1 if next_idx == index else next_idx


if __name__ == "__main__":
    array = Array()
    print(array.is_circular([2, -1, 1, 2, 2]))
    print(array.is_circular([-2, 1, -1, -2, -2]))
