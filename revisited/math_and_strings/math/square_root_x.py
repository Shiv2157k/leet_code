

class SquareRoot:

    def results(self, x: int) -> int:
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

        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

    def result(self, x: int) -> int:
        """
        Approach: Binary Search 2 to x // 2
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param x:
        :return:
        """
        # base case
        if x < 2:
            return x

        left, right = 0, x // 2
        while left <= right:
            # to prevent overflow
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot
        return right

    def result_(self, x: int):
        """
        Approach: Newton's Method
        Formulae: x(k + 1) = 1/2[x(k) + x / x(k)]
        Time Complexity: O()
        Space Complexity: O()
        :param x:
        :return:
        """
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2
        return int(x1)


if __name__ == "__main__":
    square_root = SquareRoot()
    print(square_root.result(4))
    print(square_root.result_(4))
    print(square_root.results(4))
    print(square_root.result(16))
    print(square_root.result_(16))
    print(square_root.results(16))
    print(square_root.result(300))
    print(square_root.result_(300))
    print(square_root.results(300))