from typing import List


class LastStoneWeight:

    def available(self, stones: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(M * N)
        M - total stones
        N - total weight // 2
        Space Complexity: O(N)
        :param stones:
        :return:
        """

        total_weight = 0
        for weight in stones:
            total_weight += weight

        max_weight = 0
        dp = [True] + [False] * (total_weight // 2)

        for weight in stones:
            next_state = dp[:]
            for curr_weight in range(weight, total_weight // 2 + 1):
                if dp[curr_weight - weight]:
                    next_state[curr_weight] = True
                    max_weight = max(max_weight, curr_weight)
                    if max_weight == total_weight // 2:
                        return total_weight - max_weight * 2
            # move to next state
            dp = next_state
        return total_weight - max_weight * 2


if __name__ == "__main__":
    last_stone_weight = LastStoneWeight()
    print(last_stone_weight.available([2, 7, 4, 1, 8, 1]))
    print(last_stone_weight.available([31, 26, 33, 21, 40]))