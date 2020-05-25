class RomanToInteger:
    mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
              'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_to_integer_1(self, roman: str) -> int:
        """
        Approach: Right Pass
        :param roman:
        :return:
        """
        total = self.lookup.get(roman[-1])
        for i in reversed(range(len(roman) - 1)):
            if self.lookup[roman[i]] < self.lookup[roman[i + 1]]:
                total -= self.lookup[roman[i]]
            else:
                total += self.lookup[roman[i]]
        return total

    def roman_to_integer_2(self, roman: str) -> int:
        """
        Approach: lookup
        :param roman:
        :return:
        """

        total = i = 0
        while i < len(roman):
            if i + 1 < len(roman) and self.lookup[roman[i]] < self.lookup[roman[i + 1]]:
                total += self.lookup[roman[i + 1]] - self.lookup[roman[i]]
                i += 2
            else:
                total += self.lookup[roman[i]]
                i += 1
        return total

    def roman_to_integer_3(self, roman: str) -> int:
        """
        Approach: mapper
        :param roman:
        :return:
        """
        total = i = 0
        while i < len(roman):
            if i < len(roman) - 1 and roman[i:i + 2] in self.mapper:
                total += self.mapper[roman[i:i + 2]]
                i += 2
            else:
                total += self.mapper[roman[i]]
                i += 1
        return total


if __name__ == "__main__":
    integer = RomanToInteger()
    print(integer.roman_to_integer_1('MMCMLXXXIX'))
    print(integer.roman_to_integer_2('MMCMLXXXIX'))
    print(integer.roman_to_integer_3('MMCMLXXXIX'))
