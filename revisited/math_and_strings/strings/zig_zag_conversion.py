

class ZigZag:

    def convert(self, s: str, num_rows: int) -> str:
        """
        Approach: Visit By Row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param num_rows:
        :return:
        """
        # base case
        if num_rows == 1:
            return s
        res = []
        cycle = 2 * num_rows - 2
        for row in range(num_rows):
            for idx in range(row, len(s), cycle):
                res.append(s[idx])
                # for the internal rows
                in_row_idx = idx + cycle - 2 * row
                if row != 0 and row != num_rows - 1 and in_row_idx < len(s):
                    res.append(s[in_row_idx])
        return "".join(res)

    def convert_(self, s: str, num_rows: int) -> str:
        """
        Approach: Sort By Row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param num_rows:
        :return:
        """
        # base case
        if num_rows == 1 or num_rows >= len(s):
            return s

        res = [[] for _ in range(num_rows)]
        # to keep track of direction
        delta = - 1
        row = 0
        for ch in s:
            res[row].append(ch)
            # if this is th 1st or last row
            # time to flip the direction
            if row == 0 or row == num_rows - 1:
                delta *= -1
            row += delta

        # lets join the strings of each row
        for idx in range(len(res)):
            res[idx] = "".join(res[idx])
        return "".join(res)


if __name__ == "__main__":
    zigzag = ZigZag()
    print(zigzag.convert("PAYPALISHIRING", 3))
    print(zigzag.convert_("PAYPALISHIRING", 3))
    print(zigzag.convert("PAYPALISHIRING", 4))
    print(zigzag.convert_("PAYPALISHIRING", 4))