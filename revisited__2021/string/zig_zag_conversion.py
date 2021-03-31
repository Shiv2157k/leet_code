class ZigZag:

    def convert_(self, s: str, num_rows: int) -> str:
        """
        Approach: Visit By Row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param num_rows:
        :return:
        """

        # validation
        if num_rows == 1 or num_rows >= len(s):
            return s
        result = []
        cycle = 2 * num_rows - 2

        for row in range(num_rows):
            for curr in range(row, len(s), cycle):
                result.append(s[curr])
                mid_row_index = curr + cycle - 2 * row
                if row != 0 and row != num_rows - 1 and mid_row_index < len(s):
                    result.append(s[mid_row_index])
        return "".join(result)

    def convert(self, s: str, num_rows: int) -> str:
        """
        Approach: Sort by Row
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :param num_rows:
        :return:
        """
        # validation
        if num_rows == 1 or num_rows >= len(s):
            return s

        row = 0
        delta = -1
        result = [[] for _ in range(num_rows)]

        for char in s:
            result[row].append(char)
            if row == 0 or row == num_rows - 1:
                delta *= -1
            row += delta

        for i in range(len(result)):
            result[i] = "".join(result[i])

        return "".join(result)


if __name__ == "__main__":
    zigzag = ZigZag()
    print(zigzag.convert_("PAYPALISHIRING", 3))
    print(zigzag.convert("PAYPALISHIRING", 3))
    print(zigzag.convert_("PAYPALISHIRING", 4))
    print(zigzag.convert("PAYPALISHIRING", 4))