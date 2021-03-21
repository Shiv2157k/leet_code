from typing import List


class Trucks:

    def maximum_units(self, box_types: List[List[int]], truck_size: int) -> int:
        """
        Approach: Sorting
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param box_types:
        :param truck_size:
        :return:
        """
        # sort the box type based on units
        box_types = sorted(box_types, key=lambda x: x[1], reverse=True)
        max_units = 0

        for boxes, units in box_types:
            if truck_size <= 0:
                break
            box_taken = min(truck_size, boxes)
            max_units += (box_taken * units)
            truck_size -= box_taken
        return max_units


if __name__ == "__main__":
    trucks = Trucks()
    print(trucks.maximum_units(
        [
            [1, 3], [2, 2], [3, 1]
        ], 4
    ))
    print(trucks.maximum_units(
        [
            [5, 10], [2, 5], [4, 7], [3, 9]
        ], 10
    ))
