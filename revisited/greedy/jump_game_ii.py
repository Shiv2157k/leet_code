from typing import List


class JumpGame:

    def get_minimum_jumps(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        size = len(nums)
        if size < 2:
            return 0

        max_steps = max_pos = nums[0]
        jumps = 1
        for idx in range(1, size):
            if max_steps < idx:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[idx] + idx)
        return jumps


if __name__ == "__main__":
    jump_game = JumpGame()
    print(jump_game.get_minimum_jumps([2, 3, 1, 1, 4]))
    print(jump_game.get_minimum_jumps([2, 1, 1, 1, 4]))