

class Roman:

    def __init__(self):
        self.mapper = {
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

    def to_integer(self, s: str) -> int:
        """
        Approach: Right to Left pass
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        total = self.mapper.get(s[-1])
        for i in range(len(s) - 2, -1, -1):
            if self.mapper.get(s[i]) < self.mapper.get(s[i + 1]):
                total -= self.mapper.get(s[i])
            else:
                total += self.mapper.get(s[i])
        return total


if __name__ == "__main__":
    roman = Roman()
    print(roman.to_integer("MCMXCIV"))
    print(roman.to_integer("MIII"))

