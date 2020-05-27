
class SquareRoot:

    def get_square_root_(self, val: int) -> int:
        """
        Approach: Pocket Calculator
        input: val, output: res
        Formulae:
        left-------------right
        res^2 <= val < (res + 1)
        :param val:
        :return:
        """
        from math import e, log

        left = int(e ** (0.5 * log(val)))
        right = left + 1
        return left if right * right > val else right

    def get_square_root__(self, val: int) -> int:
        """
        Approach: Binary Search
        input: val, output: res
        Formulae: 0 < x < x // 2
        :param val:
        :return:
        """
        # base case
        if val <= 2:
            return val

        left, right = 2, val // 2
        while left <= right:
            pivot = left + (right - left) // 2
            res = pivot * pivot
            if res < val:
                left = pivot + 1
            elif res > val:
                right = pivot - 1
            else:
                return pivot
        return right

    def get_square_root(self, val: int) -> int:
        """
        Approach: Newton's Method
        Formulae:
        val(k + 1) = 1/2[val(k) + val/val(k)]
        :param val:
        :return:
        """
        if val < 2:
            return val

        val0 = val
        val1 = (val0 + val / val0) / 2
        while abs(val0 - val1) >= 1:
            val0 = val1
            val1 = (val0 + val / val0) / 2
        return int(val1)


if __name__ == "__main__":
    sq = SquareRoot()
    print(sq.get_square_root(36))
    print(sq.get_square_root_(36))
    print(sq.get_square_root__(36))
    print(sq.get_square_root(10))
    print(sq.get_square_root_(10))
    print(sq.get_square_root__(10))