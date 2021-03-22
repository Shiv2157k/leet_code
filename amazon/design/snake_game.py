from typing import List
from collections import deque


class SnakeGame:
    """
    W - Width, H - Height, N - no. of food items
    Time Complexity:
        - move method : O(1)
        - calculate bite itself: O(1) using dictionary
        - add and remove element from queue: O(1)
    Space Complexity:
        - O(W * H + N)
        - O(N) - food data structure
        - O(W * H) used by snake and snake grid.
    """

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize data structure here.
        :param width:
            - screen width.
        :param height:
            - screen height.
        :param food:
            - a list of food position.
            eg: food = [[1,1], [1,0]]
        """
        # initially snake is at origin or front
        self.snake = deque([(0, 0)])
        self.snake_grid = {(0, 0): 1}
        self.height = height
        self.width = width
        self.food_index = 0
        self.food = food
        self.movement = {"U": [-1, 0], "L": [0, -1], "R": [0, 1], "D": [1, 0]}

    def move(self, direction: str) -> int:
        """
        Move the snake.
        :param direction:
            - "U" = up, "L" = left, "R" = right, "D" = down
        :return:
            game's score after move.
            -1 if game over snake crosses screen boundary or bites itself.
        """
        # build the new head provided the direction
        new_head = (self.snake[0] + self.movement[direction][0],
                    self.snake[1] + self.movement[direction][1])

        # boundary conditions
        height_boundary_crossed = new_head[0] < 0 or new_head[1] >= self.height
        width_boundary_crossed = new_head[1] < 0 or new_head[1] >= self.width

        # bites itself
        bites_itself = new_head in self.snake_grid and new_head != self.snake[-1]

        # check the boundary conditions
        if height_boundary_crossed or width_boundary_crossed or bites_itself:
            return -1

        # note food list could be empty
        next_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None

        # if there is an available food item it is on cell occupied by snake after the move, eat it
        if self.food_index < len(self.food) and next_food_item[0] == new_head[0] and next_food_item[1] == new_head[1]:
            self.food_index += 1
        else:  # time to pop the tail and remove it from snake grid
            tail = self.snake.pop()
            del self.snake[tail]

        # add the new head
        self.snake.appendleft(new_head)
        # add it to the snake grid for tracking
        self.snake_grid[new_head] = 1
        return len(self.snake) - 1
