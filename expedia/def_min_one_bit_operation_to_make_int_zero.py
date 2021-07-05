

class Integer:

    def min_one_bit_operation(self, n: int) -> int:
        """
        Approach: Iterative
        :param n:
        :return:
        """

        x = "{0:b}".format(n)
        y = list(x)
        result = 0
        is_right = True

        for k in range(len(y)):

            if x[k] == "1" and is_right:
                result += (2**(len(y) - k)) - 1
                is_right = False
            elif x[k] == "1":
                result -= (2**(len(y) - k)) - 1
                is_right = True
        return result


if __name__ == "__main__":
    integer = Integer()
    print(integer.min_one_bit_operation(3))