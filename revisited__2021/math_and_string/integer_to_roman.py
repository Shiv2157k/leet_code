

class Integer:

    converter = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                 (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                 (5, "V"), (4, "IV"), (1, "I")]

    def to_roman(self, num: int) -> str:
        """
        Approach: Greedy
        Time Complexity: O(1) as there are finite number of roman values
        Space Complexity: O(1)
        :param num:
        :return:
        """

        roman = []

        for val, symbol in self.converter:

            if num == 0:
                break
            count = num // val
            num = num % val

            roman.append(symbol * count)
        return "".join(roman)


if __name__ == "__main__":
    integer = Integer()
    print(integer.to_roman(1994))
    print(integer.to_roman(1000))
    print(integer.to_roman(90))
    print(integer.to_roman(3999))


