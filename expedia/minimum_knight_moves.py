from collections import deque
from functools import lru_cache


class Knight:

    def minimum_moves(self, x: int, y: int) -> int:
        """
        Approach: DFS
        Time Complexity: O(|x*y|)
        Space Complexity: O(|x*y|)
        :param x:
        :param y:
        :return:
        """

        @lru_cache(maxsize=None)
        def dfs(x, y):

            # base case
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2

            return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(x, y)

    def minimum_moves_(self, x: int, y: int) -> int:
        """
        Approach: BFS Bi-directional
        Time Complexity: O(max(|x|, |y|)^2)
        Space Complexity: O(max(|x|, |y|)^2)
        :param x:
        :param y:
        :return:
        """

        offsets = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1))

        # circle radar from origin
        origin_q = deque([(0, 0, 0)])
        origin_dist = {(0, 0): 0}

        # circle radar from target
        target_q = deque([(x, y, 0)])
        target_dist = {(x, y): 0}

        while True:

            origin_x, origin_y, origin_steps = origin_q.popleft()

            if (origin_x, origin_y) in target_dist:
                return origin_steps + target_dist[(origin_x, origin_y)]

            target_x, target_y, target_steps = target_q.popleft()

            if (target_x, target_y) in origin_dist:
                return target_steps + origin_dist[(target_x, target_y)]

            for off_x, off_y in offsets:

                next_origin_x, next_origin_y = origin_x + off_x, origin_y + off_y
                if (next_origin_x, next_origin_y) not in origin_dist:
                    origin_q.append((next_origin_x, next_origin_y, origin_steps + 1))
                    origin_dist[(next_origin_x, next_origin_y)] = origin_steps + 1

                next_target_x, next_target_y = target_x + off_x, target_y + off_y
                if (next_target_x, next_target_y) not in target_dist:
                    target_q.append((next_target_x, next_target_y, target_steps + 1))
                    target_dist[(next_target_x, next_target_y)] = target_steps + 1

    def minimum_moves___(self, x: int, y: int) -> int:
        """
        Approach: BFS
        Time Complexity: O(max(|x|, |y|)^2)
        Space Complexity: O(max(|x|, |y|)^2)
        :param x:
        :param y:
        :return:
        """

        offsets = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

        def bfs(x, y):

            q = deque([(0, 0)])
            steps = 0
            visited = set()
            while q:
                curr_level_count = len(q)
                for _ in range(curr_level_count):
                    curr_x, curr_y = q.popleft()

                    if (curr_x, curr_y) == (x, y):
                        return steps
                    for offset_x, offset_y in offsets:
                        next_x, next_y = curr_x + offset_x, curr_y + offset_y
                        if (next_x, next_y) not in visited:
                            q.append((next_x, next_y))
                            visited.add((next_x, next_y))

                steps += 1

        return bfs(x, y)


if __name__ == "__main__":

    knight = Knight()
    print(knight.minimum_moves_(5, 5))
    print(knight.minimum_moves(5, 5))