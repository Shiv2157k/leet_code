from typing import List

class String:

    def compress(self, chars: List[str]) -> List[str]:
        """
        Approach:
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param chars:
        :return:
        """

        writer = anchor = 0

        for reader, char in enumerate(chars):

            if reader + 1 == len(chars) or chars[reader + 1] != char:
                chars[writer] = chars[anchor]
                writer += 1
                if reader > anchor:
                    for digit in str(reader - anchor + 1):
                        chars[writer] = digit
                        writer += 1
                anchor = reader + 1
        return writer