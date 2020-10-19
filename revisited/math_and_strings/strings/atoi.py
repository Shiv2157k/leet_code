

class Atoi:

    def get_integers(self, s: str) -> int:
        """
        Approach: Scan from left to right
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        # strips whitespaces
        s = s.strip()
        if not s:
            return 0

        is_negative = False
        res = 0

        if s[0] == "-":
            is_negative = True
        elif s[0] == "+":
            is_negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            res = ord(s[0]) - ord("0")

        for idx in range(1, len(s)):

            if s[idx].isnumeric():
                res = res * 10 + (ord(s[idx]) - ord("0"))

                if not is_negative and res >= 2**31 - 1:
                    return 2**31 - 1
                if is_negative and res >= 2**31:
                    return -2**31
            else:
                break
        return res if not is_negative else -res


if __name__ == "__main__":
    atoi = Atoi()
    print(atoi.get_integers("     916 Hello"))
    print(atoi.get_integers("-2157"))
    print(atoi.get_integers("This is 123 test"))
    print(atoi.get_integers("+19"))
    print(atoi.get_integers("-999999999999999999999"))
    print(atoi.get_integers("+999999999999999999999"))