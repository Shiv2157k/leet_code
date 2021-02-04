class SquareRoot:

    def answer(self, x: int) -> int:
        """
        Approach: Binary Search
        Condition: 0 < 1 < x / 2
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param x:
        :return:
        """
        if x < 2:
            return x
        left, right = 0, x // 2

        while left < right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot
        return right

    def answer_(self, x: int) -> int:
        """
        Approach: Pocket Calculator
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param x:
        :return:
        """
        from math import e, log

        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1

        return left if right * right > x else right


if __name__ == "__main__":
    square_root = SquareRoot()
    print(square_root.answer(8))
    print(square_root.answer(4))
    print(square_root.answer(26))
    print("--------------------")
    print(square_root.answer_(8))
    print(square_root.answer_(4))
    print(square_root.answer_(26))