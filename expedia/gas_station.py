from typing import List


class GasStation:

    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param gas:
        :param cost:
        :return:
        """

        total_tank = current_tank = starting_point = 0

        for i, fuel in enumerate(gas):
            total_tank += fuel - cost[i]
            current_tank += fuel - cost[i]

            if current_tank < 0:
                current_tank = 0
                starting_point = i + 1
        return starting_point if total_tank >= 0 else -1


if __name__ == "__main__":
    gas_station = GasStation()
    print(gas_station.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
