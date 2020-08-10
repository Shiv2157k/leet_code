class Converter:

    def one(self, num: int) -> str:
        """
        Converts single digit numbers.
        :param num:
        :return:
        """
        switcher = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        return switcher.get(num)

    def two_lt_20(self, num: int) -> str:
        """
        Converts numbers less than 20.
        :param num:
        :return:
        """
        switcher = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        return switcher.get(num)

    def ten(self, num: int) -> str:
        """
        Converts 10's
        :param num:
        :return:
        """
        switcher = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        return switcher.get(num)

    def two(self, num: int) -> str:
        """
        Converts two digits.
        :param num:
        :return:
        """
        if not num:
            return ""
        elif num < 10:
            return self.one(num)
        elif num < 20:
            return self.two_lt_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return self.ten(tenner) + " " + self.one(rest) if rest else self.ten(tenner)

    def three(self, num: int) -> str:
        """
        Converts the digits greater than or equal to three.
        :param num:
        :return:
        """
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return self.one(hundred) + " Hundred " + self.two(rest)
        elif not hundred and rest:
            return self.two(rest)
        elif hundred and not rest:
            return self.one(hundred) + " Hundred"

    def integer_to_words(self, num: int) -> str:
        """
        Approach: Divide and Conquer.
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param num:
        :return:
        """
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return "Zero"

        result = ""
        if billion:
            result = self.three(billion) + " Billion"
        if million:
            result += " " if result else ""
            result += self.three(million) + " Million"
        if thousand:
            result += " " if result else ""
            result += self.three(thousand) + " Thousand"
        if rest:
            result += " " if result else ""
            result += self.three(rest)
        return result


if __name__ == "__main__":
    converter = Converter()
    print(converter.integer_to_words(123))
    print(converter.integer_to_words(12345))
    print(converter.integer_to_words(1234567))
    print(converter.integer_to_words(1234567891))


