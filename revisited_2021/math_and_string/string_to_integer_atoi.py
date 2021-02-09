

class String:

    def my_atoi(self, s: str) -> int:
        """
        Approach: Left to Right Scan
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        s = s.strip()
        if not s:
            return 0

        is_negative, result = False, 0

        if s[0] == "-":
            is_negative = True
        elif s[0] == "+":
            is_negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            result = ord(s[0]) - ord("0")

        for i in range(1, len(s)):
            if s[i].isnumeric():
                result = result * 10 + ord(s[i]) - ord("0")
                if not is_negative and result >= 2**31 - 1:
                    return 2**31 - 1
                if is_negative and result > 2**31:
                    return -2**31
            else:
                break
        return result if not is_negative else -result


if __name__ == "__main__":
    string = String()
    print(string.my_atoi(" 231 is my number"))
    print(string.my_atoi(" -321 is another number"))
    print(string.my_atoi("99999999999 there "))
