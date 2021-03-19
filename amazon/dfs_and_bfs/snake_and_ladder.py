from typing import List
from collections import deque


class SnakeAndLadder:

    def get_minimum_path(self, board: List[List[int]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        :param board:
        :return:
        """

        def get_coordinates(step: int):
            quotient, remainder = divmod(step - 1, N)
            row = N - 1 - quotient
            col = remainder if N % 2 != row % 2 else N - 1 - remainder
            return row, col

        N = len(board)
        distance_recorder = {1: 0}
        q = deque([1])

        while q:
            step = q.popleft()
            # base case
            if step == N*N:
                return distance_recorder[step]
            # move through the dice
            for next_step in range(step + 1, min(N*N, (step + 6)) + 1):
                x, y = get_coordinates(next_step)
                if board[x][y] != -1:
                    next_step = board[x][y]
                if next_step not in distance_recorder:
                    distance_recorder[next_step] = distance_recorder[step] + 1
                    q.append(next_step)
        return -1


if __name__ == "__main__":
    snake_and_ladder = SnakeAndLadder()
    print(snake_and_ladder.get_minimum_path(
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1]
        ]
    ))



