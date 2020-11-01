from typing import List


class Robot:

    def get_unique_paths_with_obstacle(self, obstacle_grid: List[List[int]]) -> int:
        """
        Approach: DP
        Time Complexity: O(M * N)
        Space Complexity: O(1)
        :param obstacle_grid:
        :return:
        """
        # base case
        if obstacle_grid[0][0] == 1:
            return 0
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        # marking the first grid to 1
        obstacle_grid[0][0] = 1

        for row in range(1, m):
            obstacle_grid[row][0] = int(obstacle_grid[row][0] == 0 and obstacle_grid[row - 1][0] == 1)

        for col in range(1, n):
            obstacle_grid[0][col] = int(obstacle_grid[0][col] == 0 and obstacle_grid[0][col - 1] == 1)

        for row in range(1, m):
            for col in range(1, n):
                if obstacle_grid[row][col] == 0:
                    obstacle_grid[row][col] = obstacle_grid[row - 1][col] + obstacle_grid[row][col - 1]
                else:
                    obstacle_grid[row][col] = 0
        return obstacle_grid[-1][-1]


if __name__ == "__main__":
    robot = Robot()
    print(robot.get_unique_paths_with_obstacle(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ))