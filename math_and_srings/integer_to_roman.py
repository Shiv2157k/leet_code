class RomanConverter:
    __mapper = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    def convert(self, number: int) -> str:
        """
        Approach: Greedy
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param number:
        :return:
        """
        output = []

        for value, roman in self.__mapper:
            if number == 0:
                break
            count, number = number // value, number % value
            output.append(roman * count)
        return "".join(output)


if __name__ == "__main__":
    int_to_roman = RomanConverter()
    print(int_to_roman.convert(58))
    print(int_to_roman.convert(900))
    print(int_to_roman.convert(958))
    print(int_to_roman.convert(1994))
