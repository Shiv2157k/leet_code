class EliminationGame:

    def last_remaining(self, n: int) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        step = head = 1
        # initially wil be moving left
        is_left = True

        while n > 1:
            # if it is moving left or
            # n is an odd number
            if is_left or n % 2 == 1:
                # head will move right by step
                head += step
            # flip the toggle to right to left
            is_left = not is_left
            # reduce n by half
            n >>= 1
            # increment step power 2
            step <<= 1
        return head


if __name__ == "__main__":
    elimination_game = EliminationGame()
    print(elimination_game.last_remaining(9))
    print(elimination_game.last_remaining(2))
    print(elimination_game.last_remaining(1))
    print(elimination_game.last_remaining(3))
    print(elimination_game.last_remaining(31))
