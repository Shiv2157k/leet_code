

class ZigZag:

    def generate_(self, s: str, row_num: int) -> str:
        """
        Approach: Visit by row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param row_num:
        :return:
        """
        if row_num == 1:
            return s
        cycle = 2 * row_num - 2
        res = []
        for i in range(row_num):
            for j in range(i, len(s), cycle):
                res.append(s[j])
                k = j + cycle - 2 * i
                if i != 0 and i != row_num - 1 and k < len(s):
                    res.append(s[k])
        return "".join(res)

    def generate(self, s: str, row_num: int) -> str:
        """
        Approach: Sort by row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param row_num:
        :return:
        """
        # base case
        if row_num == 1 or row_num >= len(s):
            return s

        result = [[] for _ in range(row_num)]
        row, delta = 0, -1
        for char in s:
            result[row].append(char)
            if row == 0 or row == row_num - 1:
                delta *= -1
            row += delta

        for idx in range(len(result)):
            result[idx] = "".join(result[idx])
        return "".join(result)


if __name__ == "__main__":
    zigzag = ZigZag()
    # P   A H   N
    # A P L S I I G
    # Y   I   R
    print(zigzag.generate("PAYPALISHIRING", 3))
    print(zigzag.generate("PAYPALISHIRING", 1))
    print(zigzag.generate_("PAYPALISHIRING", 3))
    print(zigzag.generate_("PAYPALISHIRING", 1))


