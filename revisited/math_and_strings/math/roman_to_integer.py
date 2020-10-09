class Roman:

    converter = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    def to_integer_(self, string: str) -> int:
        """
        Approach: Left to Right improvised
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        total = 0
        i = 0

        while i < len(string):
            if i < len(string) - 1 and string[i: i + 2] in self.converter:
                total += self.converter.get(string[i: i + 2])
                i += 2
            else:
                total += self.converter.get(string[i])
                i += 1
        return total

    def to_integer(self, string: str) -> int:
        """
        Approach: Right to Left Pass
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        integer = self.converter.get(string[-1])

        for idx in range(len(string) - 2, -1, -1):
            if self.converter.get(string[idx]) < self.converter.get(string[idx + 1]):
                integer -= self.converter.get(string[idx])
            else:
                integer += self.converter.get(string[idx])
        return integer


if __name__ == "__main__":
    roman = Roman()
    print(roman.to_integer("MCMXCIV"))
    print(roman.to_integer_("MCMXCIV"))