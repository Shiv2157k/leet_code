class Strings:

    def multiply(self, num1: str, num2: str) -> str:
        """
        :param num1:
        :param num2:
        :return:
        """
        res1 = res2 = 0
        for n in num1:
            res1 = res1 * 10 + (ord(n) - ord("0"))
        for n in num2:
            res2 = res2 * 10 + (ord(n) - ord("0"))
        return str(res1 * res2)

    def multiply_(self, num1: str, num2: str) -> str:
        """
        :param num1:
        :param num2:
        :return:
        """
        n1 = len(num1)
        n2 = len(num2)
        digits = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                idx = i + j
                total = digits[idx + 1] + (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                digits[idx] += total // 10
                digits[idx + 1] = total % 10
        result = ""
        for digit in digits:
            if not result and digit == 0:
                continue
            result += str(digit)
        return "0" if not result else result


if __name__ == "__main__":
    string = Strings()
    print(string.multiply_("123", "456"))
    print(string.multiply("123", "456"))