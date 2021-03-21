from typing import List


class Asteroid:

    def get_after_collision(self, asteroids: List[int]) -> List[int]:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param asteroids:
        :return:
        """
        stack = []
        for new in asteroids:
            while stack and stack[-1] > 0 > new:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:
                stack.append(new)
        return stack

    def get_after_collisions(self, asteroids: List[int]) -> List[int]:
        """
        Approach: Stack
        Time Complexity:
        Space Complexity:
        :param asteroids:
        :return:
        """

        stack = []
        for new in asteroids:
            if new > 0:
                stack.append(new)
            else:
                while stack and 0 < stack[-1] < -new:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(new)
                elif stack[-1] == -new:
                    stack.pop()
        return stack


if __name__ == "__main__":
    asteroid = Asteroid()
    print(asteroid.get_after_collisions(
        [10, -5, 5]
    ))
    print(asteroid.get_after_collisions(
        [10, 5, -5]
    ))
    print(asteroid.get_after_collision(
        [10, -5, 5]
    ))
    print(asteroid.get_after_collision(
        [10, 5, -5]
    ))
