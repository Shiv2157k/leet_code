from typing import List


class JumpGame:

    def can_jump(self, nums: List[int]) -> bool:
        """
        Approach: Greedy Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        max_reach, length = 0, len(nums)
        for index in range(length):
            if nums[index] + index > max_reach:
                max_reach = nums[index] + index
            if max_reach == index:
                break
        return max_reach >= length - 1


if __name__ == "__main__":
    jump_game = JumpGame()
    print(jump_game.can_jump([2, 3, 1, 1, 4]))
    print(jump_game.can_jump([3, 2, 1, 0, 4]))