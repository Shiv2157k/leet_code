from typing import List
from collections import deque


class City:

    def number_of_provinces_bfs(self, is_connected: List[List[int]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param is_connected:
        :return:
        """
        provinces = 0
        visited = set()

        q = deque()

        for left in range(len(is_connected)):
            if left not in visited:
                q.append(left)
                while q:
                    curr = q.popleft()
                    if curr not in visited:
                        visited.add(curr)
                    for neighbor in range(len(is_connected)):
                        if is_connected[curr][neighbor] and neighbor not in visited:
                            q.append(neighbor)
                provinces += 1
        return provinces

    def number_of_provinces_dfs(self, is_connected: List[List[int]]) -> int:
        """
        Approach: DFS
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param is_connected:
        :return:
        """
        provinces = 0
        visited = set()

        def depth_first_search(left: int):
            # base case
            if left not in visited:
                visited.add(left)
            for right in range(len(is_connected)):
                if is_connected[left][right] and right not in visited:
                    depth_first_search(right)

        for left in range(len(is_connected)):
            if left not in visited:
                provinces += 1
                depth_first_search(left)
        return provinces


if __name__ == "__main__":
    city = City()
    print(city.number_of_provinces_dfs(
    [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    ))
    print(city.number_of_provinces_dfs(
    [
        [1, 1, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]
    ))
    print(city.number_of_provinces_dfs(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    ))
    print(city.number_of_provinces_bfs(
        [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
    ))
    print(city.number_of_provinces_bfs(
        [
            [1, 1, 0],
            [1, 1, 0],
            [1, 1, 1]
        ]
    ))
    print(city.number_of_provinces_bfs(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    ))