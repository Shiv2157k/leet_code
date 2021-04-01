

class Atoi:

    def str_to_integer(self, s: str) -> int:
        """
        Approach: Scan left to right
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        s = s.strip()
        if not s:
            return 0

        is_negative, number = False, 0

        # scan through the filter
        if s[0] == "-":
            is_negative = True
        elif s[0] == "+":
            is_negative = False
        elif not s[0].isnumeric():
            return number
        else:
            number = ord(s[0]) - ord("0")

        for idx in range(1, len(s)):
            if s[idx].isnumeric():
                number = number * 10 + ord(s[idx]) - ord("0")

                if not is_negative and number >= 2**31 - 1:
                    return 2**31 - 1
                if is_negative and number >= 2**31:
                    return -2**31
            else:
                break
        return number if not is_negative else -number


if __name__ == "__main__":
    atoi = Atoi()
    print(atoi.str_to_integer("2157"))
    print(atoi.str_to_integer("  - 2157"))
    print(atoi.str_to_integer("  -2157  "))
    print(atoi.str_to_integer(" +2157 "))
    print(atoi.str_to_integer("898392839283293829382"))
    print(atoi.str_to_integer("-839382784837422"))