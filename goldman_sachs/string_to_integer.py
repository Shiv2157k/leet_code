class Atoi:

    def string_to_integer(self, s: str) -> int:
        """
        Approach: Scan left to right
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        # strip the leading and trailing white spaces
        s = s.strip()

        # validation
        if not s:
            return 0

        result = 0
        is_negative = False

        if s[0] == "-":
            is_negative = True
        elif s[0] == "+":
            is_negative = False
        elif not s[0].isnumeric():
            return result
        else:
            result = ord(s[0]) - ord("0")

        for i in range(1, len(s)):
            if s[i].isnumeric():
                result = result * 10 + ord(s[i]) - ord("0")
                if not is_negative and result >= 2**31 - 1:
                    return 2**31 - 1
                if is_negative and result >= 2**31:
                    return -2**31
            else:
                break
        return result if not is_negative else -result


if __name__ == "__main__":
    atoi = Atoi()
    print(atoi.string_to_integer(" -42"))
    print(atoi.string_to_integer("ds901"))
    print(atoi.string_to_integer(" 90 1"))
    print(atoi.string_to_integer("84984394374387439383"))
    print(atoi.string_to_integer("-84984394374387439383"))