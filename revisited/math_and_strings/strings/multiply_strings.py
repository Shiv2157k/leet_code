

class Multiply:

    def strings(self, num1: str, num2: str) -> int:
        """
        Approach: using ord
        Time Complexity: O(max(num1, num2))
        Space Complexity: O(1)
        :param num1:
        :param num2:
        :return:
        """

        res1 = res2 = 0
        for digit in num1:
            res1 = res1 * 10 + (ord(digit) - ord("0"))
        for digit in num2:
            res2 = res2 * 10 + (ord(digit) - ord("0"))
        return res1 * res2


if __name__ == "__main__":
    product = Multiply()
    print(product.strings("3", "3"))
    print(product.strings("25", "25"))
    print(product.strings("120", "120"))