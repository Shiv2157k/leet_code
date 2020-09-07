from typing import List


class RoundTrip:

    def get_starting_point(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param gas:
        :param cost:
        :return:
        """
        # total tank
        #   - to keep track of total fuel need for round trip.
        # curr tank
        #   - to keep track of fuel from starting point of round trip.
        # starting_point
        #   - to keep track of a valid starting point.
        total_tank = current_tank = starting_point = 0

        for i, fuel in enumerate(gas):

            total_tank += fuel - cost[i]
            current_tank += fuel - cost[i]

            # if the current tank is less than 0
            # won't be able to make a round trip
            # reset the starting point and the gas
            # found in that station
            if current_tank < 0:
                current_tank = 0
                starting_point = i + 1
        # return the starting point if there is
        # fuel in total tank at-least a point i.e.,
        # non negative
        # else -1
        return starting_point if total_tank >= 0 else -1


if __name__ == "__main__":
    round_trip = RoundTrip()
    print(round_trip.get_starting_point([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(round_trip.get_starting_point([2, 3, 4], [3, 4, 3]))