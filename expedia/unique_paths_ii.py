from typing import List


class Robot:

    def unique_path_to_reach_target(self, obstacle_grid: List[List[int]]) -> int:
        """
        Approach: DP
        Time Complexity: O(M * N)
        Space Complexity: O(1)
        :param obstacle_grid:
        :return:
        """

        rows, cols = len(obstacle_grid), len(obstacle_grid[0])

        if obstacle_grid[0][0] == 1:
            return 0

        obstacle_grid[0][0] = 1

        for row in range(1, rows):
            obstacle_grid[row][0] = int(obstacle_grid[row][0] == 0 and obstacle_grid[row - 1][0] == 1)

        for col in range(1, cols):
            obstacle_grid[0][col] = int(obstacle_grid[0][col] == 0 and obstacle_grid[0][col - 1] == 1)

        for row in range(1, rows):
            for col in range(1, cols):

                if obstacle_grid[row][col] == 0:
                    obstacle_grid[row][col] = obstacle_grid[row - 1][col] + obstacle_grid[row][col - 1]
                else:
                    obstacle_grid[row][col] = 0
        return obstacle_grid[-1][-1]


if __name__ == "__main__":
    robot = Robot()
    print(robot.unique_path_to_reach_target(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ))
    print(robot.unique_path_to_reach_target(
        [[0, 1], [0, 0]]
    ))
