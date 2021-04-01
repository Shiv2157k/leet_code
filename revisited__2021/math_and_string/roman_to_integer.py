

class Roman:

    converter = {"M": 1000, "D": 500, "C": 100, "L": 50,
                 "X": 10, "V": 5, "I": 1}

    def to_integer(self, s: str) -> int:
        """
        Approach: Right to left pass
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        total = self.converter.get(s[-1])
        for i in range(len(s) - 2, -1, -1):
            if self.converter.get(s[i]) < self.converter.get(s[i + 1]):
                total -= self.converter.get(s[i])
            else:
                total += self.converter.get(s[i])
        return total