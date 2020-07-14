from typing import List


class GasStation:

    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param gas:
        :param cost:
        :return:
        """
        total_tank = curr_tank = circuit_point = 0
        for station, fuel in enumerate(gas):
            total_tank += fuel - cost[station]
            curr_tank += fuel - cost[station]
            if curr_tank < 0:
                circuit_point = station + 1
                curr_tank = 0
        return circuit_point if total_tank >= 0 else -1


if __name__ == "__main__":
    gas_station = GasStation()
    print(gas_station.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(gas_station.can_complete_circuit([2, 3, 4], [3, 4, 3]))