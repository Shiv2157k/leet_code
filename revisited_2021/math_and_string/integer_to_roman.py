class Integer:

    def to_roman(self, num: int) -> str:
        """
        Approach: Greedy
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param num:
        :return:
        """
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        romans = []

        for value, symbol in digits:
            if num == 0:
                break
            count = num // value
            num = num % value
            # count, num = divmod(num, value
            romans.append(symbol * count)
        return "".join(romans)


if __name__ == "__main__":
    integer = Integer()
    print(integer.to_roman(295))
    print(integer.to_roman(294))
    print(integer.to_roman(1999))
    print(integer.to_roman(200))
    print(integer.to_roman(19))
