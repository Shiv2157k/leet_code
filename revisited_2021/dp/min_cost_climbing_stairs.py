from typing import List


class ClimbingStairs:

    def minimum_cost(self, costs: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param costs:
        :return:
        """
        f1 = f2 = 0
        for cost in reversed(costs):
            f1, f2 = cost + min(f1, f2), f1
        return min(f1, f2)


if __name__ == "__main__":
    climbing_stairs = ClimbingStairs()
    print(climbing_stairs.minimum_cost([10, 15, 20]))
    print(climbing_stairs.minimum_cost([100, 1, 78, 1, 90, 1, 1, 38, 1]))
    print(climbing_stairs.minimum_cost([100]))
    print(climbing_stairs.minimum_cost([1, 100]))