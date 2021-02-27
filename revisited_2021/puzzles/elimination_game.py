

class EliminationGame:

    def last_remaining(self, n: int) -> int:
        """
        Approach: Math (observation)
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        head = step = 1
        is_left = True
        while n > 1:
            # if it is left or n is an odd
            # time to move the head
            if is_left or n % 2 == 1:
                head += step

            is_left = not is_left
            # decrement the n to half
            n >>= 1
            # increment the step multiplying by 2
            step <<= 1
        return head


if __name__ == "__main__":
    elimination_game = EliminationGame()
    print(elimination_game.last_remaining(9))
    print(elimination_game.last_remaining(24))