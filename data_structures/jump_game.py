from typing import List


class JumpGame:

    def get_minimum_jumps(self, nums: List[int]) -> int:
        """
        Approach: Greedy Algorithm
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return 0
        max_pos = max_steps = nums[0]
        jumps = 1

        for index in range(1, n):
            if max_steps < index:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[index] + index)
        return jumps

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
    print(jump_game.get_minimum_jumps([2, 3, 1, 1, 4]))
    print(jump_game.get_minimum_jumps([3, 2, 1, 0, 4]))