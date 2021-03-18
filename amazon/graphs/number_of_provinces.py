from typing import List


class Province:

    def total_number(self, is_connected: List[List[int]]) -> int:
        """
        Approach: DFS
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param is_connected:
        :return:
        """
        number_of_provinces = 0
        visited = set()
        total_provinces = len(is_connected)

        def depth_first_search(start_node: int):
            # add the visited node
            visited.add(start_node)
            for neighbor in range(total_provinces):
                if is_connected[start_node][neighbor] and neighbor not in visited:
                    depth_first_search(neighbor)

        for start_node in range(total_provinces):
            if start_node not in visited:
                number_of_provinces += 1
                depth_first_search(start_node)
        return number_of_provinces


if __name__ == "__main__":
    province = Province()
    print(province.total_number(
        [
            [1, 1, 0], [1, 1, 0], [0, 0, 1]
        ]
    ))
    print(province.total_number(
        [
            [1, 0, 0], [0, 1, 0], [0, 0, 1]
        ]
    ))
