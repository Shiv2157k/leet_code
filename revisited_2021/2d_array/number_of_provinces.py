from typing import List


class Provinces:

    def total_number_of_provinces(self, is_connected: List[List[int]]) -> int:
        """
        Approach: Depth First Search
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param is_connected:
        :return:
        """
        def depth_first_search(left: int):
            visited.add(left)
            for right in range(len(is_connected)):
                if is_connected[left][right] and right not in visited:
                    depth_first_search(right)

        no_of_provinces = 0
        visited = set()
        for left in range(len(is_connected)):
            if left not in visited:
                no_of_provinces += 1
                depth_first_search(left)
        return no_of_provinces


if __name__ == "__main__":
    provinces = Provinces()
    print(provinces.total_number_of_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(provinces.total_number_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))